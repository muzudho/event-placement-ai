import random
import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def read_entry_lists():
    # print("Info    : my_lib/entry_list/read_entry_lists().")

    # Location.
    participant_csv = "./event-placement-ai/input-data/participant.csv"
    floor_map_csv = "./event-placement-ai/auto-generated/floor-map.csv"

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
    From: floor-map.csv
    -------------------
    """
    flo_df = pd.read_csv(floor_map_csv,
                         sep=',', engine='python')
    flo_id_list = flo_df["ID"].values.tolist()
    return par_id_list, flo_id_list
