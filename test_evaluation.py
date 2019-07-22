import pandas as pd
from evaluation import evaluate
from my_lib.position import new_position
from my_lib.build_floor_map import convert_floor_map

# Location.
block1_file = "./event-placement-ai/test/block-1.txt"
table1_file = "./event-placement-ai/test/table-1.txt"
floor1_file = "./event-placement-ai/test/floor-1.csv"
participant1_file = "./event-placement-ai/test/participant-1.csv"
mappings1_file = "./event-placement-ai/test/mappings-1.csv"

block2_file = "./event-placement-ai/test/block-2.txt"
table2_file = "./event-placement-ai/test/table-2.txt"
floor2_file = "./event-placement-ai/test/floor-2.csv"
participant2_file = "./event-placement-ai/test/participant-2.csv"
mappings2_file = "./event-placement-ai/test/mappings-2.csv"

# Read a floor.
floor1_df = convert_floor_map(block1_file, table1_file)
floor1_df.to_csv(floor1_file, index=False)

floor2_df = convert_floor_map(block2_file, table2_file)
floor2_df.to_csv(floor2_file, index=False)

participant1_df = pd.read_csv(participant1_file)
participant2_df = pd.read_csv(participant2_file)
mappings1_df = pd.read_csv(mappings1_file,
                           sep=',', engine='python')
mappings2_df = pd.read_csv(mappings2_file,
                           sep=',', engine='python')

low_pos = new_position(floor1_df, participant1_df, mappings1_df)
high_pos = new_position(floor2_df, participant2_df, mappings2_df)

low_value = evaluate(low_pos)
high_value = evaluate(high_pos)

if (low_value < high_value):
    print("ok.")
else:
    print("BAD.")

print("Info    : Finished.")
