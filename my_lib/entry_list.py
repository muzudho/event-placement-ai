import random
import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def read_entry_lists():

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
    pd_df = pd.read_csv(participant_csv,
                        sep=',', engine='python')
    pd_list = pd_df["ID"].values.tolist()

    """
    From: floor-map.csv
    -------------------
    """
    fl_df = pd.read_csv(floor_map_csv,
                        sep=',', engine='python')
    fl_list = fl_df["ID"].values.tolist()
    return pd_list, fl_list
