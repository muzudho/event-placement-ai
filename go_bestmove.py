import random
import pandas as pd
from my_lib.html_generator.css_builder import new_csv
from my_lib.html_generator.html_builder import new_html
from my_lib.entry_list import read_entry_lists
from my_lib.mapper import write_mappings
from my_lib.position import new_position
from my_lib.build_floor_map import convert_floor_map
from evaluation import evaluate

# Location.
input_block_file = "./event-placement-ai/input-data/floor-map-block.txt"
input_table_file = "./event-placement-ai/input-data/floor-map-table-number.txt"
best_position_file = "./event-placement-ai/output-data/best-position.csv"
output_position_file = "./event-placement-ai/auto-generated/position.csv"
floor_map_csv_file = "./event-placement-ai/auto-generated/floor-map.csv"
participant_csv_file = "./event-placement-ai/input-data/participant.csv"
mappings_csv_file = "./event-placement-ai/auto-generated/mappings.csv"

# Read a cloor map.
floor_df = convert_floor_map(input_block_file, input_table_file)
floor_df.to_csv(floor_map_csv_file, index=False)

par_id_list, flo_id_list = read_entry_lists()
# print("Info    : Participants count: {}".format(len(par_id_list)))
# print("Info    : Table        count: {}".format(len(flo_id_list)))

max_value = -1

for i in range(0, 1000):
    # Shuffule
    random.shuffle(par_id_list)
    random.shuffle(flo_id_list)

    write_mappings(par_id_list, flo_id_list)

    floor_df = pd.read_csv(floor_map_csv_file,
                           sep=',', engine='python')
    participant_df = pd.read_csv(participant_csv_file)
    mappings_df = pd.read_csv(mappings_csv_file,
                              sep=',', engine='python')

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
    pos_df.to_csv(output_position_file, index=False)

    # Evaluation
    value = evaluate(pos_df)
    print("Info    : i={}, Value={}, Max={}".format(i, value, max_value))

    if max_value < value:
        # Update and output.
        max_value = value
        new_html(pos_df)
        new_csv(pos_df)
        pos_df.to_csv(best_position_file, index=False)


print("Info    : Finished.")
