import random
import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def new_entry_lists_from_mappings(best_mappings_file):
    # print("Info    : my_lib/entry_list/new_entry_lists_from_mappings().")
    """
    From: mappings.csv
    ---------------------

    TABLE,PARTICIPANT
    1,26
    2,8
    3,39
    """
    map_df = pd.read_csv(best_mappings_file,
                         sep=',', engine='python')
    tbl_id_list = map_df["TABLE"].values.tolist()
    par_id_list = map_df["PARTICIPANT"].values.tolist()

    return tbl_id_list, par_id_list


def read_entry_lists(floor_csv, par_df):
    # print("Info    : my_lib/entry_list/read_entry_lists().")
    """
    participant.csv
    ---------
    ID,GENRE_CODE
    1,Red
    2,Red
    3,Blue
    """
    par_id_list = par_df["ID"].values.tolist()
    genre_code_list = par_df["GENRE_CODE"].values.tolist()

    """
    floor.csv
    ---------
    ID,X,Y,BLOCK
    27,0,0,C
    26,1,0,C
    25,2,0,C
    """
    tbl_df = pd.read_csv(floor_csv,
                         sep=',', engine='python')
    tbl_id_list = tbl_df["ID"].values.tolist()
    return tbl_id_list, par_id_list, genre_code_list
