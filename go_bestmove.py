import random
from my_lib.html_generator.css_builder import new_csv
from my_lib.html_generator.html_builder import new_html
from my_lib.entry_list import read_entry_lists
from my_lib.mapper import write_mappings
from my_lib.position import new_position
from build_floor_map import convert_map

# Location.
best_position = "./event-placement-ai/output-data/best-position.csv"

# Read a cloor map.
convert_map()

par_id_list, flo_id_list = read_entry_lists()
print("Info    : Participants count: {}".format(len(par_id_list)))
print("Info    : Table        count: {}".format(len(flo_id_list)))

# Shuffule
random.shuffle(par_id_list)
random.shuffle(flo_id_list)

write_mappings(par_id_list, flo_id_list)

pos_df = new_position()

new_html(pos_df)
new_csv(pos_df)

pos_df.to_csv(best_position, index=False)

print("Info    : Finished.")
