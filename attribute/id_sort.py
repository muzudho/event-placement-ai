import os
import pandas as pd


def id_sort(csv_file):
    # "{}/practice-pandas/data/test-participant.csv".format(os.getcwd())
    df = pd.read_csv(csv_file, sep=',', engine='python')

    """
    print(df.head(1000))
        ID   GENRE_CODE
    0    1          Red
    1    2          Red
    2    3         Blue
    3    4         Blue
    4    5        Green
    5    6         Blue
    6    7          Red
    7    8         Blue
    8    9        Green
    9   10        Green
    10  11       Purple
    11  12          Red
    12  13       Violet
    13  14        Green
    14  15         Blue
    15  16       Yellow
    16  17         Blue
    17  18       Yellow
    18  19      SkyBlue
    19  20       Yellow
    20  21          Red
    21  22         Blue
    22  23        Black
    23  24        Black
    24  25        White
    25  26       Yellow
    26  27         Blue
    27  28         Pink
    28  29        Green
    29  30         Blue
    30  31       Yellow
    31  32       Orange
    32  33         Blue
    33  34         Pink
    34  35         Gray
    35  36        Green
    36  37          Red
    37  38       Orange
    38  39        White
    39  40         Blue
    40  41          Red
    41  42        Green
    42  43       Yellow
    43  44        Green
    44  45  YellowGreen
    45  46        Black
    46  47        Brown
    47  48        White
    48  49         Gray
    49  50         Blue
    50  51       Yellow
    51  52          Red
    52  53        Green
    53  54       Orange
    54  55       Violet
    55  56         Blue
    56  57        Green
    57  58       Yellow
    58  59        White
    59  60         Blue
    """

    df2 = df.assign(RANK=df["GENRE_CODE"].rank())
    df3 = df2.groupby('GENRE_CODE').size().rank(
        ascending=False,
        method='first'
    ).astype(int).reset_index(name='RANK')
    df2 = df2.drop("RANK", axis=1)
    df2 = df2.merge(df3, right_index=True, on='GENRE_CODE').sort_index()
    df2 = df2.drop("ID", axis=1)
    df_grouped = df2.groupby("GENRE_CODE").count()
    df = pd.read_csv(
        "{}/practice-pandas/data/test-participant.csv".format(os.getcwd()), sep=',', engine='python')
    df2 = df.assign(RANK=df["GENRE_CODE"].rank())
    df3 = df2.groupby('GENRE_CODE').size().rank(
        ascending=False,
        method='first'
    ).astype(int).reset_index(name='RANK')
    df2 = df2.drop("RANK", axis=1)
    df2 = df2.merge(df3, right_index=True, on='GENRE_CODE').sort_index()
    df2 = df2.drop("ID", axis=1)
    df_grouped = df2.groupby("GENRE_CODE").count()
    df4 = df.merge(df_grouped, right_index=True, on='GENRE_CODE')

    """
    [[1], [2], [7], [12], [21], [37], [41], [52], [3], [4], [6], [8], [15], [17], [22], [27], [30], [33], [40], [50], [56], [60], [5], [9], [10], [14], [29], [36], [42], [44], [53], [57], [11],
    [13], [55], [16], [18], [20], [26], [31], [43], [51], [58], [19], [23], [24], [46], [25], [39], [48], [59], [28], [34], [32], [38], [54], [35], [49], [45], [47]]
    """
    return df4[["ID"]].values.tolist()
