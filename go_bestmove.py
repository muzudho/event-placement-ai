import os
import random
import pandas as pd
from my_lib.html_generator.css_builder import new_csv
from my_lib.html_generator.html_builder import new_html
from my_lib.html_generator.json_builder import new_json
from my_lib.entry_list import new_entry_lists_from_mappings
from my_lib.entry_list import read_entry_lists
from my_lib.mapper import new_mappings
from my_lib.position import new_position
from my_lib.build_floor_map import convert_floor_map
from evaluation import evaluate

# Location.
block_file = "./event-placement-ai/input-data/block.txt"
table_file = "./event-placement-ai/input-data/table.txt"
participant_file = "./event-placement-ai/input-data/participant.csv"
position_file = "./event-placement-ai/auto-generated/position-{}-{}-{}.csv"
floor_file = "./event-placement-ai/auto-generated/floor.csv"
best_mappings_file = "./event-placement-ai/auto-generated/best-mappings.csv"

# Read a floor.
floor_df = convert_floor_map(block_file, table_file)
floor_df.to_csv(floor_file, index=False)

participant_df = pd.read_csv(participant_file)

if os.path.isfile(best_mappings_file):
    tbl_id_list, par_id_list = new_entry_lists_from_mappings(
        best_mappings_file)
    # print("len(tbl_id_list): {}".format(len(tbl_id_list)))
    # print("len(par_id_list): {}".format(len(par_id_list)))
    print("tbl_id_list: {}".format(tbl_id_list))
    # print("par_id_list: {}".format(par_id_list))

    genre_code_list = []
    for i in range(0, len(tbl_id_list)):
        temp_df = participant_df[participant_df.ID == par_id_list[i]]
        temp_df = temp_df['GENRE_CODE']
        # print(temp_df.head(5))
        # print("temp_df.values.tolist()[0]: {}".format(
        #    temp_df.values.tolist()[0]))
        genre_code_list.append(temp_df.values.tolist()[0])
    # print("len(genre_code_list): {}".format(len(genre_code_list)))
    # print("genre_code_list: {}".format(genre_code_list))
else:
    tbl_id_list, par_id_list, genre_code_list = read_entry_lists(
        floor_file, participant_df)
# print("Info    : Participants count: {}".format(len(par_id_list)))
# print("Info    : Table        count: {}".format(len(tbl_id_list)))

# テーブル番号を崩さずスキャンしたいので、ソートしない。
# tbl_id_list.sort()
# random.shuffle(tbl_id_list)

# Shuffule at first.
# random.shuffle(par_id_list)

prod_num = 0
var_num = 0
progress_num = 0
retry = True
max_value = -1


def pick_up_index_list(tbl_id_list, genre_code_list):
    """
    index_list = []
    for i in range(0, len(par_id_list)):
        index_list.append(i)
    return index_list
    """

    order_list = [0] * len(tbl_id_list)
    index = 0
    for tbl_id in tbl_id_list:
        order_list[tbl_id-1] = index
        index += 1

    print("order_list: {}".format(order_list))

    index_list = []
    prev_genre_code = None
    prev_index = -1
    # 同じジャンルコードが連続しているところは、始点と終点だけを取る。
    for order, index in enumerate(order_list):
        genre_code = genre_code_list[index]

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

    #print("len(genre_code_list)-1: {}".format(len(genre_code_list)-1))
    index_list.append(order_list[len(order_list)-1])
    print("index_list: {}".format(index_list))

    # # 並び順を崩さないようにすること。
    # # result = list(set(index_list))
    # # print("result: {}".format(result))
    return index_list


def swap_par(index11, index12, tbl_id_list, par_id_list, genre_code_list):
    index1 = index_list[index11]
    index2 = index_list[index12]

    temp_tbl_id = tbl_id_list[index1]
    temp_par_id = par_id_list[index1]
    temp_genre_code = genre_code_list[index1]

    tbl_id_list[index1] = tbl_id_list[index2]
    par_id_list[index1] = par_id_list[index2]
    genre_code_list[index1] = genre_code_list[index2]

    tbl_id_list[index2] = temp_tbl_id
    par_id_list[index2] = temp_par_id
    genre_code_list[index2] = temp_genre_code
    return


while retry:
    retry = False
    for i in range(0, 1000):
        progress_num += 1

        # Pick up table.
        index_list = pick_up_index_list(tbl_id_list, genre_code_list)
        print("pick up index_list: {}".format(index_list))

        # Random swap.
        size = len(index_list)
        index1 = random.randint(0, size-1)
        index2 = random.randint(0, size-1)
        # print("size={}, index1={}, index2={}".format(size, index1, index2))
        swap_par(index1, index2, tbl_id_list, par_id_list, genre_code_list)

        mappings_df = new_mappings(tbl_id_list, par_id_list)

        pos_df = new_position(floor_df,
                              participant_df, mappings_df)

        # Evaluation
        value = evaluate(pos_df)
        print("Info    : i={}, Value={}, Max={}".format(i, value, max_value))

        if max_value < value:
            # Update and output.
            max_value = value
            new_html(pos_df, prod_num, var_num, progress_num, max_value)
            new_csv(pos_df, prod_num, var_num, progress_num)
            new_json(pos_df, prod_num, var_num, progress_num, max_value)
            mappings_df.to_csv(best_mappings_file, index=False)
            pos_df.to_csv(position_file.format(
                prod_num, var_num, progress_num), index=False)
            retry = True
        else:
            # Cancel swap.
            swap_par(index2, index1, tbl_id_list, par_id_list, genre_code_list)
            """
            temp = par_id_list[index2]
            par_id_list[index2] = par_id_list[index1]
            par_id_list[index1] = temp
            """

print("Info    : Finished.")
