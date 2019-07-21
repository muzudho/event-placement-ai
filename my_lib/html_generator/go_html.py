import pandas as pd

#
# Note.
#
# Root directory: Visual studio code workspace root.
#
html_file = "./event-placement-ai/auto-generated/view.html"


def new_html(pos_df):
    def get_boxes(pos_df):
        html = []
        for _index, row in pos_df.iterrows():
            html.append(
                """
        <div id="table{}">{}</div>
                """.format(row["TABLE"], row["PARTICIPANT"])
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
