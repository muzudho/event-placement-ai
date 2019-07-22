import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def new_position(floor_map_csv_file, participant_csv_file, mappings_csv_file):
    """
    Create position.
    """
    # print("Info    : my_lib/position/new_position().")

    """
    floor-map.csv
    --------------------

    ID,X,Y,BLOCK
    27,0,0,C
    26,1,0,C
    25,2,0,C
    """
    flo_df = pd.read_csv(floor_map_csv_file,
                         sep=',', engine='python')
    # print("Info    : floor-map.csv : {}".format(floor_map_csv_file))
    # print(flo_df.head(100))

    """
    participant.csv
    -----------------------

    ID,GENRE_CODE
    1,Red
    2,Red
    3,Blue
    """
    par_df = pd.read_csv(participant_csv_file)
    # print("Info    : participant.csv : {}".format(participant_csv_file))
    # print(par_df.head(100))

    """
    mappings.csv
    ------------------------

    PARTICIPANT,TABLE
    45,35
    23,27
    57,47
    """
    map_df = pd.read_csv(mappings_csv_file,
                         sep=',', engine='python')
    # print("Info    : Mappings DF: {}".format(map_df.shape))
    # print("Info    : mappings.csv : {}".format(mappings_csv_file))
    # print(map_df.head(100))

    new_df = flo_df.merge(map_df, left_on='ID', right_on='TABLE', how='outer')
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

    new_df = new_df.merge(par_df, left_on='PARTICIPANT',
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
