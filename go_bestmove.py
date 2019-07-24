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
best_position_file = "./event-placement-ai/output-data/best-position.csv"
position_file = "./event-placement-ai/auto-generated/position.csv"
floor_file = "./event-placement-ai/auto-generated/floor.csv"
participant_file = "./event-placement-ai/input-data/participant.csv"
best_mappings_file = "./event-placement-ai/auto-generated/best-mappings.csv"

# Read a floor.
floor_df = convert_floor_map(block_file, table_file)
floor_df.to_csv(floor_file, index=False)

if os.path.isfile(best_mappings_file):
    tbl_id_list, par_id_list = new_entry_lists_from_mappings(
        best_mappings_file)
else:
    tbl_id_list, par_id_list = read_entry_lists(floor_file, participant_file)
# print("Info    : Participants count: {}".format(len(par_id_list)))
# print("Info    : Table        count: {}".format(len(tbl_id_list)))

# Sort table.
tbl_id_list.sort()
# random.shuffle(tbl_id_list)

# Shuffule at first.
# random.shuffle(par_id_list)

max_value = -1

for i in range(0, 1000):
    # Swap.
    size = len(par_id_list)
    index1 = random.randint(0, size-1)
    index2 = random.randint(0, size-1)
    # print("size={}, index1={}, index2={}".format(size, index1, index2))
    temp = par_id_list[index1]
    par_id_list[index1] = par_id_list[index2]
    par_id_list[index2] = temp

    mappings_df = new_mappings(tbl_id_list, par_id_list)

    participant_df = pd.read_csv(participant_file)

    pos_df = new_position(floor_df,
                          participant_df, mappings_df)

    """
    output
    ------

    X,Y,BLOCK,PARTICIPANT,TABLE,GENRE_CODE
    0,0,C,1,27,Red
    1,0,C,2,26,Red
    2,0,C,3,25,Blue
    3,0,C,4,24,Blue
    4,0,C,5,23,Green
    """
    pos_df.to_csv(position_file, index=False)

    # Evaluation
    value = evaluate(pos_df)
    print("Info    : i={}, Value={}, Max={}".format(i, value, max_value))

    if max_value < value:
        # Update and output.
        max_value = value
        new_html(pos_df, 0, 0, max_value)
        new_csv(pos_df, 0, 0)
        new_json(pos_df, 0, 0, max_value)
        mappings_df.to_csv(best_mappings_file, index=False)
        pos_df.to_csv(best_position_file, index=False)
    else:
        # Cancel swap.
        temp = par_id_list[index2]
        par_id_list[index2] = par_id_list[index1]
        par_id_list[index1] = temp


print("Info    : Finished.")
