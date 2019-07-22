from evaluation import evaluate
from my_lib.position import new_position

# Location.
floor1_file = "./event-placement-ai/test/floor-1.csv"
participant1_file = "./event-placement-ai/test/participant-1.csv"
mappings1_file = "./event-placement-ai/test/mappings-1.csv"

floor2_file = "./event-placement-ai/test/floor-2.csv"
participant2_file = "./event-placement-ai/test/participant-2.csv"
mappings2_file = "./event-placement-ai/test/mappings-2.csv"

low_pos = new_position(floor1_file, participant1_file, mappings1_file)
high_pos = new_position(floor2_file, participant2_file, mappings2_file)

low_value = evaluate(low_pos)
high_value = evaluate(high_pos)

if (low_value < high_value):
    print("ok.")
else:
    print("BAD.")

print("Info    : Finished.")
