import random
from my_lib.html_generator.css_builder import new_csv
from my_lib.html_generator.html_builder import new_html
from my_lib.entry_list import read_entry_lists
from my_lib.mapper import write_mappings
from my_lib.position import new_position
from my_lib.build_floor_map import convert_map
from evaluation import evaluate

# Location.
best_position_file = "./event-placement-ai/output-data/best-position.csv"

# Read a cloor map.
convert_map()

par_id_list, flo_id_list = read_entry_lists()
# print("Info    : Participants count: {}".format(len(par_id_list)))
# print("Info    : Table        count: {}".format(len(flo_id_list)))

max_value = -1
best_pos_df = None

for i in range(0, 1000):
    # Shuffule
    random.shuffle(par_id_list)
    random.shuffle(flo_id_list)

    write_mappings(par_id_list, flo_id_list)

    pos_df = new_position()

    # Evaluation
    value = evaluate(pos_df)
    print("Info    : Value={}, Max={}".format(value, max_value))

    if max_value < value:
        max_value = value
        best_pos_df = pos_df

new_html(best_pos_df)
new_csv(best_pos_df)

best_pos_df.to_csv(best_position_file, index=False)

print("Info    : Finished.")
