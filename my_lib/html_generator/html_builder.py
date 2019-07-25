import pandas as pd

#
# Note.
#
# Root directory: Visual studio code workspace root.
#


def new_html(pos_df, test_number, variation_number, progress_num, value):
    # print("Info    : my_lib/html_generator/html_builder/new_html().")
    # print("Info    : pos_df.shape : {}".format(pos_df.shape))

    # Location.
    html_file = "./event-placement-ai/auto-generated/placement-{}-{}-{}.html"

    def get_boxes(pos_df):
        html = []
        for _index, row in pos_df.iterrows():
            table_id = row["TABLE"]
            participants_id = row["PARTICIPANT"]
            # print("Info    : TABLE={}, PARTICIPANT={}".format(
            #    table_id, participants_id))

            html.append(
                """
        <div id="table{}">{}</div>
                """.format(table_id, participants_id)
            )
        return "".join(html)

    try:
        file = open(html_file.format(
            test_number, variation_number, progress_num), 'w', encoding='utf-8')
        file.write(
            """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="placement-{0}-{1}-{2}.css">
    <title>placement-{0}-{1}-{2}</title>
</head>
<body>
    <h1>Value={4}</h1>
    <div id="floor-map">
{3}
    </div>
</body>
</html>
            """.format(test_number, variation_number, progress_num, get_boxes(pos_df), value)
        )
    except Exception as e:
        print(e)
    finally:
        file.close()
