import pandas as pd
from evaluation import evaluate
from my_lib.position import new_position
from my_lib.build_floor_map import convert_floor_map


def make_position(test_number, variation_number):
    # Location.
    block_file = "./event-placement-ai/test/block-{}.txt".format(
        test_number)
    table_file = "./event-placement-ai/test/table-{}.txt".format(
        test_number)
    # floor_file = "./event-placement-ai/test/floor-{}.csv".format(test_number, variation_number)
    participant_file = "./event-placement-ai/test/participant-{}.csv".format(
        test_number)
    mappings_file = "./event-placement-ai/test/mappings-{}-{}.csv".format(
        test_number, variation_number)

    # Read a floor.
    floor_df = convert_floor_map(block_file, table_file)
    # floor_df.to_csv(floor_file, index=False)

    participant_df = pd.read_csv(participant_file)

    mappings_df = pd.read_csv(mappings_file,
                              sep=',', engine='python')
    return new_position(floor_df, participant_df, mappings_df)


low_value = evaluate(make_position(1, 1))
high_value = evaluate(make_position(1, 2))

if (low_value < high_value):
    print("ok.")
else:
    print("BAD.")

print("Info    : Finished.")
