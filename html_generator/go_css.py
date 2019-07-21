import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def new_csv():
    """
    Create csv.
    """

    # Output.
    output_css = "./event-placement-ai/html_generator/auto-generated/table-color.css"

    """
    Input: floor-map.csv
    --------------------

    ID,X,Y,BLOCK
    27,0,0,C
    26,1,0,C
    25,2,0,C
    """
    fl_df = pd.read_csv("./event-placement-ai/auto-generated/floor-map.csv",
                        sep=',', engine='python')
    # print(fl_df.values.tolist())

    """
    Input: participants.csv
    -----------------------

    ID,GENRE_CODE
    1,Red
    2,Red
    3,Blue
    """
    pa_df = pd.read_csv(
        "./event-placement-ai/html_generator/input/participant.csv")

    """
    Auto-generated: Mappings
    ------------------------

    ID,GENRE_CODE
    1,Red
    2,Red
    3,Blue
    """
    ma_df = pd.read_csv("./event-placement-ai/html_generator/auto-generated/mappings.csv",
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

    """
    New-table: new2_df
    ------------------

    print(new2_df.head(3))

        ID_x GENRE_CODE  PARTICIPANT  TABLE  ID_y   X  Y BLOCK
    0     30       Blue           30     30    30   0  3     C
    1      6       Blue            6      6     6  18  5     A
    2     56       Blue           56     56    56   3  2     F
    """
    new2_df = new_df.merge(fl_df, left_on='TABLE', right_on='ID')

    def write():
        try:
            file = open(output_css, 'w', encoding='utf-8')
            file.write(
                """
    {}
                """.format(get_boxes())
            )
        except Exception as e:
            print(e)
        finally:
            file.close()

    def get_boxes():
        html = []
        for _index, new2_row in new2_df.iterrows():

            # Participant id.
            id = new2_row["PARTICIPANT"]
            # print("     id : {}".format(id))
            # print("type(id): {}".format(type(id)))

            x = new2_row["X"]
            y = new2_row["Y"]

            width = 16
            height = 16

            html.append(
                """
    #box{} {{
        position: absolute;
        left    : {: >4}px;
        top     : {: >4}px;
        width   : {: >4}px;
        height  : {: >4}px;
        background-color: {};
    }}
                """.format(
                    id,
                    x * width,
                    y * height,
                    width,
                    height,
                    new2_row["GENRE_CODE"])
            )

        return "".join(html)

    write()
