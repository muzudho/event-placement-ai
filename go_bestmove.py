import os
import random
import pandas as pd
from my_lib.html_generator.css_builder import new_csv
from my_lib.html_generator.html_builder import new_html
from my_lib.html_generator.json_builder import new_json
from my_lib.html_generator.json_builder import write_json
from my_lib.entry_list import new_entry_lists_from_mappings
from my_lib.entry_list import read_entry_lists
from my_lib.mapper import new_mappings
from my_lib.position import new_position
from my_lib.position import Position
from my_lib.search import Search
from my_lib.relocation import shift_smaller
from my_lib.relocation import shift_bigger
from my_lib.relocation import swap_participant
from my_lib.relocation import choice_index
from my_lib.relocation import count_joined_genre_code
from my_lib.build_floor_map import convert_floor_map
from evaluation import evaluate

# Location.
block_file = "./event-placement-ai/input-data/block.txt"
table_file = "./event-placement-ai/input-data/table.txt"
participant_file = "./event-placement-ai/input-data/participant.csv"
position_file = "./event-placement-ai/auto-generated/position-{}-{}-{}.csv"
floor_file = "./event-placement-ai/auto-generated/floor.csv"
best_mappings_file = "./event-placement-ai/auto-generated/best-mappings.csv"

"""
floor.csv
---------

ID,X,Y,BLOCK
27,0,0,C
26,1,0,C
25,2,0,C

- ID順にソートすると、BLOCKも固まるようにしてください。
"""
floor_df = convert_floor_map(block_file, table_file)
floor_df = floor_df.sort_values(by=["ID"], ascending=True)
floor_df.to_csv(floor_file, index=False)

position = Position()

"""
block_names = ['A', 'B', 'C', 'D', 'E', 'F']
"""
for _index, row in floor_df.iterrows():
    block = row["BLOCK"]
    position.block_list.append(block)
    position.block_names.append(block)

# 重複は無くなるが、順はバラバラになる。
position.block_names = list(set(position.block_names))
print("block_names: {}.".format(position.block_names))

participant_df = pd.read_csv(participant_file)

if os.path.isfile(best_mappings_file):
    position.tbl_id_list, position.par_id_list = new_entry_lists_from_mappings(
        best_mappings_file)
    # print("len(tbl_id_list): {}".format(len(position.tbl_id_list)))
    # print("len(par_id_list): {}".format(len(position.par_id_list)))
    # print("tbl_id_list: {}".format(position.tbl_id_list))
    # print("par_id_list: {}".format(position.par_id_list))

    for i in range(0, len(position.tbl_id_list)):
        temp_df = participant_df[participant_df.ID == position.par_id_list[i]]
        temp_df = temp_df['GENRE_CODE']
        # print(temp_df.head(5))
        # print("temp_df.values.tolist()[0]: {}".format(
        #    temp_df.values.tolist()[0]))
        position.genre_code_list.append(temp_df.values.tolist()[0])
    # print("len(genre_code_list): {}".format(len(position.genre_code_list)))
    # print("genre_code_list: {}".format(position.genre_code_list))
else:
    position.tbl_id_list, position.par_id_list, position.genre_code_list = read_entry_lists(
        floor_file, participant_df)
    # テーブルIDは固定。参加者はシャッフル。
    for size in reversed(range(2, len(position.par_id_list)-1)):
        index1 = random.randint(0, size-1)
        index2 = random.randint(0, size-1)
        temp = position.par_id_list[index1]
        position.par_id_list[index1] = position.par_id_list[index2]
        position.par_id_list[index2] = temp

    # random.shuffle(position.par_id_list)

# print("Info    : Participants count: {}".format(len(position.par_id_list)))
# print("Info    : Table        count: {}".format(len(position.tbl_id_list)))

# テーブル番号を崩さずスキャンしたいので、ソートしない。
# position.tbl_id_list.sort()

# Shuffule at first.

search = Search()


def update_best():
    """
    最善の局面を更新。
    """
    new_html(pos_df, search.prod_num, search.var_num,
             search.progress_num, search.max_value)
    new_csv(pos_df, search.prod_num, search.var_num, search.progress_num)

    json = new_json(search.prod_num, search.var_num,
                    search.progress_num, search.max_value)
    write_json(search.prod_num, search.var_num, search.progress_num, json)

    mappings_df.to_csv(best_mappings_file, index=False)
    pos_df.to_csv(position_file.format(
        search.prod_num, search.var_num, search.progress_num), index=False)
    return


while search.retry:
    search.retry = False

    for i in range(0, 1000):

        if i % 50 == 0:
            # シフトを試してみる。
            mappings_df = new_mappings(
                position.tbl_id_list, position.par_id_list)
            pos_df = new_position(floor_df,
                                  participant_df, mappings_df)
            value = evaluate(pos_df)
            print("Info    : Before shift, Value={}, Max={}".format(
                value, search.max_value))

            # 先頭から連続するブロック数を求めます。
            result_dict = count_joined_genre_code(position)

            # 1個だけシフト。 TODO 連続するブロック数だけシフトしたい。
            shift_smaller(position)
            mappings_df = new_mappings(
                position.tbl_id_list, position.par_id_list)
            pos_df = new_position(floor_df,
                                  participant_df, mappings_df)
            value = evaluate(pos_df)
            if search.max_value < value:
                # Update and output.
                search.max_value = value
                update_best()
                search.retry = True
            else:
                # Cancel swap.
                shift_bigger(position)

        search.progress_num += 1

        index1, index2 = choice_index(position)

        swap_participant(index1, index2, position)

        mappings_df = new_mappings(position.tbl_id_list, position.par_id_list)

        pos_df = new_position(floor_df,
                              participant_df, mappings_df)

        # Evaluation
        value = evaluate(pos_df)
        print("Info    : i={}, Value={}, Max={}".format(
            i, value, search.max_value))

        if search.max_value < value:
            # Update and output.
            search.max_value = value
            update_best()
            search.retry = True
        else:
            # Cancel swap.
            swap_participant(index2, index1, position)

print("Info    : Finished.")
