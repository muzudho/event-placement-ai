import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def new_position():
    """
    Create position.
    """

    # Location.
    output_position = "./event-placement-ai/auto-generated/position.csv"
    input_floor = "./event-placement-ai/auto-generated/floor-map.csv"
    input_participant = "./event-placement-ai/input-data/participant.csv"
    mappings_file = "./event-placement-ai/auto-generated/mappings.csv"

    """
    Input: floor-map.csv
    --------------------

    ID,X,Y,BLOCK
    27,0,0,C
    26,1,0,C
    25,2,0,C
    """
    fl_df = pd.read_csv(input_floor,
                        sep=',', engine='python')

    """
    Input: participants.csv
    -----------------------

    ID,GENRE_CODE
    1,Red
    2,Red
    3,Blue
    """
    pa_df = pd.read_csv(input_participant)

    """
    Auto-generated: Mappings
    ------------------------

    ID,GENRE_CODE
    1,Red
    2,Red
    3,Blue
    """
    ma_df = pd.read_csv(mappings_file,
                        sep=',', engine='python')

    """
    New-table: new_df
    -----------------

    Join.
    print(new_df.head(3))

        ID GENRE_CODE  PARTICIPANT  TABLE
    0   30       Blue           30     30
    1    6       Blue            6      6
    2   56       Blue           56     56
    """
    new_df = pa_df.merge(ma_df, left_on='ID', right_on='PARTICIPANT')
    new_df = new_df.drop("ID", axis=1)

    """
    New-table: new2_df
    ------------------

    print(new2_df.head(3))

        GENRE_CODE  PARTICIPANT  TABLE  ID   X  Y BLOCK
    0         Blue           30     30  30   0  3     C
    1         Blue            6      6   6  18  5     A
    2         Blue           56     56  56   3  2     F
    """
    new2_df = new_df.merge(fl_df, left_on='TABLE', right_on='ID')
    new2_df = new2_df.drop("ID", axis=1)

    """
    output
    ------

GENRE_CODE,PARTICIPANT,TABLE,X,Y,BLOCK
Red,1,31,0,4,C
Red,2,25,2,0,C
Blue,3,8,19,4,A
    """
    new2_df.to_csv(output_position, index=False)

    return new2_df
