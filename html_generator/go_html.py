import pandas as pd
from attribute.query_id_sorted_table import query_id_sorted_table

#
# Note.
#
# Root directory: Visual studio code workspace root.
#
file_name = "./html-generator/auto-generated/view.html"
df = pd.read_csv("./html-generator/data/participant.csv",
                 sep=',', engine='python')
# Data frame. (Not record set)
df = query_id_sorted_table("./html-generator/data/participant.csv")
"""
print(df.values.tolist())
[[30, 'Blue'], [6, 'Blue'], [56, 'Blue'], [50, 'Blue'], [40, 'Blue'], [33, 'Blue'], [27, 'Blue'], [22, 'Blue'], [17, 'Blue'], [15, 'Blue'], [8, 'Blue'], [4, 'Blue'], [3, 'Blue'], [60, 'Blue'], [5, 'Green'], [10, 'Green'], [14, 'Green'], [9, 'Green'], [29, 'Green'], [36, 'Green'], [42, 'Green'], [44, 'Green'], [53, 'Green'], [57, 'Green'], [16, 'Yellow'], [20, 'Yellow'], [26, 'Yellow'], [31, 'Yellow'], [43, 'Yellow'], [51, 'Yellow'], [58, 'Yellow'], [18, 'Yellow'], [1, 'Red'], [7, 'Red'], [2, 'Red'], [52, 'Red'], [41, 'Red'], [37, 'Red'], [21, 'Red'], [12, 'Red'], [59, 'White'], [48, 'White'], [39, 'White'], [25, 'White'], [54, 'Orange'], [46, 'Black'], [24, 'Black'], [23, 'Black'], [32, 'Orange'], [38, 'Orange'], [35, 'Gray'], [49, 'Gray'], [13, 'Violet'], [34, 'Pink'], [28, 'Pink'], [55, 'Violet'], [19, 'SkyBlue'], [11, 'Purple'], [45, 'YellowGreen'], [47, 'Brown']]
"""


def write():
    try:
        file = open(file_name, 'w', encoding='utf-8')
        file.write(
            """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="participants.css">
    <title>サンプル</title>
</head>
<body>
{}
</body>
</html>
            """.format(get_boxes(df))
        )
    except Exception as e:
        print(e)
    finally:
        file.close()


def get_boxes(df):
    html = []
    for _index, row in df.iterrows():
        html.append(
            """
    <div id="box{}">
    </div>
            """.format(row["ID"])
        )
    return "".join(html)


write()
