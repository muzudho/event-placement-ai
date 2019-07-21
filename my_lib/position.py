import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def new_position():
    """
    Create position.
    """
    print("Info    : my_lib/position/new_position().")

    # Location.
    output_position = "./event-placement-ai/auto-generated/position.csv"
    input_floor = "./event-placement-ai/auto-generated/floor-map.csv"
    input_participant = "./event-placement-ai/input-data/participant.csv"
    mappings_file = "./event-placement-ai/auto-generated/mappings.csv"

    """
    floor-map.csv
    --------------------

    ID,X,Y,BLOCK
    27,0,0,C
    26,1,0,C
    25,2,0,C
    """
    flo_df = pd.read_csv(input_floor,
                         sep=',', engine='python')
    print("Info    : floor-map.csv : {}".format(input_floor))
    print(flo_df.head(100))

    """
    participant.csv
    -----------------------

    ID,GENRE_CODE
    1,Red
    2,Red
    3,Blue
    """
    par_df = pd.read_csv(input_participant)
    print("Info    : participant.csv : {}".format(input_participant))
    print(par_df.head(100))

    """
    mappings.csv
    ------------------------

    PARTICIPANT,TABLE
    45,35
    23,27
    57,47
    """
    map_df = pd.read_csv(mappings_file,
                         sep=',', engine='python')
    print("Info    : Mappings DF: {}".format(map_df.shape))
    print("Info    : mappings.csv : {}".format(mappings_file))
    print(map_df.head(100))

    new_df = flo_df.merge(map_df, left_on='ID', right_on='TABLE', how='outer')
    print("Info    : Join1.")
    print(new_df.head(100))
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
    print("Info    : Join2.")
    print(new_df.head(100))
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

    new_df.to_csv(output_position, index=False)
    """
    X,Y,BLOCK,PARTICIPANT,TABLE,GENRE_CODE
    0,0,C,1,27,Red
    1,0,C,2,26,Red
    2,0,C,3,25,Blue
    3,0,C,4,24,Blue
    4,0,C,5,23,Green
    """

    print("Info    : Position DF: {}".format(new_df.shape))

    return new_df
