import pandas as pd
from evaluation import evaluate
from my_lib.position import new_position

# Location.
floor1_file = "./event-placement-ai/test/floor-1.csv"
participant1_file = "./event-placement-ai/test/participant-1.csv"
mappings1_file = "./event-placement-ai/test/mappings-1.csv"

floor2_file = "./event-placement-ai/test/floor-2.csv"
participant2_file = "./event-placement-ai/test/participant-2.csv"
mappings2_file = "./event-placement-ai/test/mappings-2.csv"

floor1_df = pd.read_csv(floor1_file,
                        sep=',', engine='python')
floor2_df = pd.read_csv(floor2_file,
                        sep=',', engine='python')
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
