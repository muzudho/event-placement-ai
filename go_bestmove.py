from html_generator.go_css import new_csv
from my_lib.entry_list import read_entry_lists
from my_lib.shuffuling import go_shuffule
from my_lib.position import new_position


pd_list, fl_list = read_entry_lists()
go_shuffule(pd_list, fl_list)
pos_df = new_position()
new_csv(pos_df)
print("Info    : Finished.")
