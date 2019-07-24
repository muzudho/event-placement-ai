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


def read_entry_lists(floor_csv, participant_csv):
    # print("Info    : my_lib/entry_list/read_entry_lists().")
    """
    From: Participant.csv
    ---------------------

    ID,GENRE_CODE
    1,Red
    2,Red
    3,Blue
    """
    par_df = pd.read_csv(participant_csv,
                         sep=',', engine='python')
    par_id_list = par_df["ID"].values.tolist()

    """
    From: floor.csv
    ---------------
    """
    tbl_df = pd.read_csv(floor_csv,
                         sep=',', engine='python')
    tbl_id_list = tbl_df["ID"].values.tolist()
    return tbl_id_list, par_id_list
