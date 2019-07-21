from my_lib.html_generator.go_css import new_csv
from my_lib.html_generator.go_html import new_html
from my_lib.entry_list import read_entry_lists
from my_lib.shuffuling import go_shuffule
from my_lib.position import new_position

# Location.
best_position = "./event-placement-ai/output-data/best-position.csv"

par_id_list, flo_id_list = read_entry_lists()
go_shuffule(par_id_list, flo_id_list)
pos_df = new_position()
new_html(pos_df)
new_csv(pos_df)

pos_df.to_csv(best_position, index=False)

print("Info    : Finished.")
