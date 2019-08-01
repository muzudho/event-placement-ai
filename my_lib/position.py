import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def new_position(floor_df, participant_df, mappings_df):
    """
    Create position.
    """
    # print("Info    : my_lib/position/new_position().")

    """
    floor_df
    --------

    ID,X,Y,BLOCK
    27,0,0,C
    26,1,0,C
    25,2,0,C
    """
    # print("Info    : floor.csv : {}".format(floor_map_csv_file))
    # print(flo_df.head(100))

    """
    participant.csv
    -----------------------

    ID,GENRE_CODE
    1,Red
    2,Red
    3,Blue
    """
    # print("Info    : participant.csv : {}".format(participant_df))
    # print(par_df.head(100))

    """
    mappings.csv
    ------------------------

    PARTICIPANT,TABLE
    45,35
    23,27
    57,47
    """
    # print("Info    : Mappings DF: {}".format(mappings_df.shape))
    # print("Info    : mappings.csv : {}".format(mappings_df))
    # print(mappings_df.head(100))

    new_df = floor_df.merge(mappings_df, left_on='ID',
                            right_on='TABLE', how='outer')
    # print("Info    : Join1.")
    # print(new_df.head(100))
    """
    new_df
    ------
    ID  X  Y BLOCK  PARTICIPANT  TABLE
    0  27  0  0     C            1     27
    1  26  1  0     C            2     26
    2  25  2  0     C            3     25
    """

    new_df = new_df.drop("ID", axis=1)
    """
    new_df
    ------

     X  Y BLOCK  PARTICIPANT  TABLE
    27  0  0     C            1     27
    26  1  0     C            2     26
    25  2  0     C            3     25
    """

    new_df = new_df.merge(participant_df, left_on='PARTICIPANT',
                          right_on='ID', how='outer')
    # print("Info    : Join2.")
    # print(new_df.head(100))
    """
       X  Y BLOCK  PARTICIPANT  TABLE  ID GENRE_CODE
    0  0  0     C            1     27   1        Red
    1  1  0     C            2     26   2        Red
    2  2  0     C            3     25   3       Blue
    """

    new_df = new_df.drop("ID", axis=1)

    """
    new_df
    ------

       X  Y BLOCK  PARTICIPANT  TABLE GENRE_CODE
    0  0  0     C            1     27        Red
    1  1  0     C            2     26        Red
    2  2  0     C            3     25       Blue
    """

    # print("Info    : Position DF: {}".format(new_df.shape))

    return new_df


class Position(object):
    """
    局面。
    """

    def __init__(self):
        self._block_list = []
        self._block_names = []
        self._genre_code_list = []
        return

    @property
    def block_list(self):
        return self._block_list

    @block_list.setter
    def block_list(self, value):
        self._block_list = value

    @property
    def block_names(self):
        return self._block_names

    @block_names.setter
    def block_names(self, value):
        self._block_names = value

    @property
    def genre_code_list(self):
        return self._genre_code_list

    @genre_code_list.setter
    def genre_code_list(self, value):
        self._genre_code_list = value
