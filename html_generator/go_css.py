import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def new_csv(pos_df):
    """
    Create csv.
    """

    # Location.
    output_css = "./event-placement-ai/auto-generated/table-color.css"

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
        for _index, row in pos_df.iterrows():

            # Participant id.
            id = row["PARTICIPANT"]
            # print("     id : {}".format(id))
            # print("type(id): {}".format(type(id)))

            x = row["X"]
            y = row["Y"]

            width = 16
            height = 16

            html.append(
                """
    #table{} {{
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
                    row["GENRE_CODE"])
            )

        return "".join(html)

    write()
