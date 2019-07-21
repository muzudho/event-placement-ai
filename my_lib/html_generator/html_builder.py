import pandas as pd

#
# Note.
#
# Root directory: Visual studio code workspace root.
#
html_file = "./event-placement-ai/auto-generated/view.html"


def new_html(pos_df):
    # print("Info    : my_lib/html_generator/html_builder/new_html().")
    # print("Info    : pos_df.shape : {}".format(pos_df.shape))

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
        file = open(html_file, 'w', encoding='utf-8')
        file.write(
            """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="table-color.css">
    <title>サンプル</title>
</head>
<body>
{}
</body>
</html>
            """.format(get_boxes(pos_df))
        )
    except Exception as e:
        print(e)
    finally:
        file.close()
