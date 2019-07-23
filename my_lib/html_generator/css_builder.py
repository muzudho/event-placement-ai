import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def new_csv(pos_df, test_number, variation_number):
    """
    Create csv.
    """
    # print("Info    : my_lib/html_generator/css_builder/new_csv().")

    # Location.
    output_css = "./event-placement-ai/auto-generated/placement-{}-{}.css"

    def write():

        def get_boxes():
            html = []
            for _index, row in pos_df.iterrows():

                table_id = row["TABLE"]
                # print("     id : {}".format(id))
                # print("type(id): {}".format(type(id)))

                x = row["X"]
                y = row["Y"]

                width = 32
                height = 32

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
                        table_id,
                        x * width,
                        y * height,
                        width,
                        height,
                        row["GENRE_CODE"])
                )

            return "".join(html)

        try:
            file = open(output_css.format(
                test_number, variation_number), 'w', encoding='utf-8')
            file.write(
                """
#floor-map {{
    position: relative;
    left    : 0px;
    top     : 0px;
}}

{}
                """.format(get_boxes())
            )
        except Exception as e:
            print(e)
        finally:
            file.close()

    write()
