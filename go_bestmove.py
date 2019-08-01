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
    position.tbl_id_list, par_id_list = new_entry_lists_from_mappings(
        best_mappings_file)
    # print("len(tbl_id_list): {}".format(len(position.tbl_id_list)))
    # print("len(par_id_list): {}".format(len(par_id_list)))
    # print("tbl_id_list: {}".format(position.tbl_id_list))
    # print("par_id_list: {}".format(par_id_list))

    for i in range(0, len(position.tbl_id_list)):
        temp_df = participant_df[participant_df.ID == par_id_list[i]]
        temp_df = temp_df['GENRE_CODE']
        # print(temp_df.head(5))
        # print("temp_df.values.tolist()[0]: {}".format(
        #    temp_df.values.tolist()[0]))
        position.genre_code_list.append(temp_df.values.tolist()[0])
    # print("len(genre_code_list): {}".format(len(position.genre_code_list)))
    # print("genre_code_list: {}".format(position.genre_code_list))
else:
    position.tbl_id_list, par_id_list, position.genre_code_list = read_entry_lists(
        floor_file, participant_df)
    # テーブルIDは固定。参加者はシャッフル。
    for size in reversed(range(2, len(par_id_list)-1)):
        index1 = random.randint(0, size-1)
        index2 = random.randint(0, size-1)
        temp = par_id_list[index1]
        par_id_list[index1] = par_id_list[index2]
        par_id_list[index2] = temp

    # random.shuffle(par_id_list)

# print("Info    : Participants count: {}".format(len(par_id_list)))
# print("Info    : Table        count: {}".format(len(position.tbl_id_list)))

# テーブル番号を崩さずスキャンしたいので、ソートしない。
# position.tbl_id_list.sort()

# Shuffule at first.

prod_num = 0
var_num = 0
progress_num = 0
retry = True
max_value = -1


def pick_up_index_list(position):
    """
    index_list = []
    for i in range(0, len(par_id_list)):
        index_list.append(i)
    return index_list
    """

    order_list = [0] * len(position.tbl_id_list)
    index = 0
    for tbl_id in position.tbl_id_list:
        order_list[tbl_id-1] = index
        index += 1

    # print("order_list: {}".format(order_list))

    index_list = []
    prev_genre_code = None
    prev_index = -1
    # 同じジャンルコードが連続しているところは、始点と終点だけを取る。
    for index in order_list:
        genre_code = position.genre_code_list[index]

        # print("prev_genre_code: {}, genre_code: {}".format(
        #    prev_genre_code, genre_code))
        if prev_genre_code == None:
            prev_genre_code = genre_code

            # Index of start.
            index_list.append(index)

        elif prev_genre_code != genre_code:
            prev_genre_code = genre_code
            # print("start: {}, end: {}".format(
            #    start, current-1))

            if index_list[len(index_list)-1] != prev_index:
                # Index of previous end.
                index_list.append(prev_index)

            # Index of start.
            index_list.append(index)

        prev_index = index

    # print("len(genre_code_list)-1: {}".format(len(position.genre_code_list)-1))
    index_list.append(order_list[len(order_list)-1])
    # print("index_list: {}".format(index_list))

    # # 並び順を崩さないようにすること。
    # # result = list(set(index_list))
    # # print("result: {}".format(result))
    return index_list


def choice_index():
    # Pick up table.
    picked_up_index_list = pick_up_index_list(position)
    # print("picked_up_index_list: {}".format(picked_up_index_list))

    # リトライ回数が多すぎると、終わりたいときに、逆に終わらないかもしれない。
    retry = 3
    genre_code1 = None
    genre_code2 = None
    while genre_code1 == genre_code2 and 0 < retry:
        # Random choice at first.
        size = len(picked_up_index_list)
        index11 = random.randint(0, size-1)
        index1 = picked_up_index_list[index11]
        genre_code1 = position.genre_code_list[index1]

        # 同じ色はなるべく選ばない。
        index12 = random.randint(0, size-1)
        index2 = picked_up_index_list[index12]
        genre_code2 = position.genre_code_list[index2]
        retry -= 1

    # print("size={}, index1={}, index2={}".format(size, index1, index2))
    # print("Choiced index1={}, index2={}".format(index1, index2))
    return index1, index2


def swap_participant(index1, index2, par_id_list, position):
    """
    テーブルＩＤは固定し、参加者ＩＤを入れ替えます。
    """
    temp_par_id = par_id_list[index1]
    temp_genre_code = position.genre_code_list[index1]

    par_id_list[index1] = par_id_list[index2]
    position.genre_code_list[index1] = position.genre_code_list[index2]

    par_id_list[index2] = temp_par_id
    position.genre_code_list[index2] = temp_genre_code
    return


def shift_smaller():
    """
    ブロック単位でシフトします。[1,2,3,4]を、[2,3,4,1]にする動きです。
    """

    prev_block = None
    # テーブルID順に並んでいるとします。
    for index, block in enumerate(position.block_list):
        # for index, row in floor_df.iterrows():
        if prev_block == block:
            swap_participant(
                index-1, index, par_id_list, position)

        prev_block = block

    return


def shift_bigger():
    """
    ブロック単位でシフトします。[1,2,3,4]を、[4, 1, 2, 3]にする動きです。
    """

    prev_block = None
    index = len(position.block_list)-1
    # テーブルID順に並んでいるとします。
    for block in reversed(position.block_list):
        # print("shift_bigger: index={}, block={}.".format(index, block))
        if prev_block == block:
            swap_participant(
                index, index+1, par_id_list, position)

        prev_block = block
        index -= 1

    return


def for_block_asc(callback_head_block, callback_same_block):
    """
    ブロックの切れ目が分かるループです。昇順。
    """
    # テーブルID順に並んでいるとします。
    prev_block = None
    for i in range(0, len(position.block_list)):
        if prev_block == position.block_list[i]:
            callback_same_block(i, position.block_list[i])
        else:
            callback_head_block(i, position.block_list[i])
        prev_block = position.block_list[i]
    return


def for_block_desc(callback_tail_block, callback_same_block):
    """
    ブロックの切れ目が分かるループです。降順。
    """
    # テーブルID順に並んでいるとします。
    prev_block = None
    for i in reversed(range(0, len(position.block_list))):
        if prev_block == position.block_list[i]:
            callback_same_block(i, position.block_list[i])
        else:
            callback_tail_block(i, position.block_list[i])
        prev_block = position.block_list[i]
    return


'''
def count_joined_genre_code():
    """
    TODO 同じブロック内での、連続するジャンルコードの数。
    """

    count = 0
    result_dict = {}
    prev_block = None
    prev_genre_code = None
    for idx in range(0, len(position.block_list)):
        block = position.block_list[idx]
        genre_code = position.genre_code_list[idx]
        if prev_block != block or prev_genre_code != genre_code:
            result_dict[prev_block] = count
            count = 0
        else:
            count += 1

        prev_block = block
        prev_genre_code = genre_code

    return
'''


def update_best():
    """
    最善の局面を更新。
    """
    new_html(pos_df, prod_num, var_num, progress_num, max_value)
    new_csv(pos_df, prod_num, var_num, progress_num)

    json = new_json(prod_num, var_num, progress_num, max_value)
    write_json(prod_num, var_num, progress_num, json)

    mappings_df.to_csv(best_mappings_file, index=False)
    pos_df.to_csv(position_file.format(
        prod_num, var_num, progress_num), index=False)
    return


while retry:
    retry = False

    for i in range(0, 1000):

        if i % 50 == 0:
            # シフトを試してみる。
            mappings_df = new_mappings(position.tbl_id_list, par_id_list)
            pos_df = new_position(floor_df,
                                  participant_df, mappings_df)
            value = evaluate(pos_df)
            print("Info    : Before shift, Value={}, Max={}".format(value, max_value))
            shift_smaller()
            mappings_df = new_mappings(position.tbl_id_list, par_id_list)
            pos_df = new_position(floor_df,
                                  participant_df, mappings_df)
            value = evaluate(pos_df)
            if max_value < value:
                # Update and output.
                max_value = value
                update_best()
                retry = True
            else:
                # Cancel swap.
                shift_bigger()

        progress_num += 1

        index1, index2 = choice_index()

        swap_participant(index1, index2, par_id_list, position)

        mappings_df = new_mappings(position.tbl_id_list, par_id_list)

        pos_df = new_position(floor_df,
                              participant_df, mappings_df)

        # Evaluation
        value = evaluate(pos_df)
        print("Info    : i={}, Value={}, Max={}".format(i, value, max_value))

        if max_value < value:
            # Update and output.
            max_value = value
            update_best()
            retry = True
        else:
            # Cancel swap.
            swap_participant(index2, index1, par_id_list, position)

print("Info    : Finished.")
