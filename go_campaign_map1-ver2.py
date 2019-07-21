from html_generator.go_css import new_csv
from my_lib.entry_list import read_entry_lists
from my_lib.shuffuling import go_shuffule


pd_list, fl_list = read_entry_lists()
go_shuffule(pd_list, fl_list)
new_csv()
print("Info    : Finished.")
