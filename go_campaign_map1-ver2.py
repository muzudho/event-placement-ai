import random
import pandas as pd
from html_generator.go_css import new_csv

"""
Note.
    Root directory: Visual studio code workspace root.
"""


"""
From: Participant.csv
---------------------

ID,GENRE_CODE
1,Red
2,Red
3,Blue
"""
pd_df = pd.read_csv("./event-placement-ai/data/participant.csv",
                    sep=',', engine='python')
pd_list = pd_df["ID"].values.tolist()
random.shuffle(pd_list)
# print("pd_list: {}".format(pd_list))

"""
From: floor-map.csv
-------------------
"""
fl_df = pd.read_csv("./event-placement-ai/auto-generated/floor-map.csv",
                    sep=',', engine='python')
fl_list = fl_df["ID"].values.tolist()
random.shuffle(fl_list)
# print("fl_list: {}".format(fl_list))


"""
Make: mappings.csv
------------------

PARTICIPANT,TABLE
57,25
38,26
6,8
"""
try:
    output_mappings = "./event-placement-ai/html_generator/auto-generated/mappings.csv"
    file = open(output_mappings, 'w', encoding='utf-8')

    file.write("PARTICIPANT,TABLE\n")
    for i in range(len(pd_list)):
        file.write(
            "{},{}\n".format(pd_list[i], fl_list[i])
        )
except Exception as e:
    print(e)
finally:
    file.close()


new_csv()

print("Info    : Finished.")
