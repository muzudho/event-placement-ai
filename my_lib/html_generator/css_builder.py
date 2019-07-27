import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def new_csv(pos_df, test_number, variation_number, progress_num):
    """
    Create csv.
    """
    # print("Info    : my_lib/html_generator/css_builder/new_csv().")

    # Location.
    output_css = "./event-placement-ai/auto-generated/placement-{}-{}-{}.css"

    def write():

        def get_boxes():
            css = []
            area_width = 0
            area_height = 0

            for _index, row in pos_df.iterrows():

                table_id = row["TABLE"]
                # print("     id : {}".format(id))
                # print("type(id): {}".format(type(id)))

                width = 32
                height = 32

                x = row["X"] * width
                y = row["Y"] * height

                if area_width < x+width:
                    area_width = x+width

                if area_height < y+height:
                    area_height = y+height

                css.append(
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
                        x,
                        y,
                        width,
                        height,
                        row["GENRE_CODE"])
                )

            return "".join(css), area_width, area_height

        try:
            file = open(output_css.format(
                test_number, variation_number, progress_num), 'w', encoding='utf-8')

            boxes, area_width, area_height = get_boxes()

            file.write(
                """
#data {{
    position: relative;
    left    :   0px;
    top     :   0px;
    width   : 100%;
    height  : 100px;
}}

#floor-map {{
    position: relative;
    left    :      0px;
    top     :      0px;
    width   : {1: >4}px;
    height  : {2: >4}px;
}}

{0}
                """.format(boxes, area_width, area_height)
            )
        except Exception as e:
            print(e)
        finally:
            file.close()

    write()
