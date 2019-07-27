def evaluate(pos_df):
    """
    position.csv
    ------------

X,Y,BLOCK,TABLE,PARTICIPANT,GENRE_CODE
0,0,C,27,2,Red
1,0,C,26,1,Red
2,0,C,25,37,Red
    """

    # 評価値
    value = 0

    # block_dict[block][genre_code] = value
    block_dict = {}

    for _index, row in pos_df.iterrows():
        # x = row["X"]
        # y = row["Y"]
        block = row["BLOCK"]
        # table_id = row["TABLE"]
        # participant_id = row["PARTICIPANT"]
        genre_code = row["GENRE_CODE"]

        if not(block in block_dict):
            block_dict[block] = {}

        if not(genre_code in block_dict[block]):
            block_dict[block][genre_code] = 0

        block_dict[block][genre_code] += 1

    # 集計。ブロックに同じ色が集まっているほど高評価。
    for _block_name, genre_code_dict in block_dict.items():
        for _genre_code_name, count in genre_code_dict.items():
            value += count ** 2
            break

    # 集計。テーブル番号順にして、同じ色が連続したら、連続した数だけ加点。
    # ただし、ブロックの切れ目は連続しない。
    continue_bonus = 0
    sorted_pos_df = pos_df.sort_values(by=["TABLE"], ascending=True)
    # print(sorted_pos_df.head(5))
    table_ordered_list = sorted_pos_df[[
        "TABLE", "BLOCK", "GENRE_CODE"]].values.tolist()
    # print("table_ordered_list: {}".format(table_ordered_list))
    prev_block = None
    prev_genre_code = None
    for entry in table_ordered_list:
        if prev_genre_code == entry[2] and prev_block == entry[1]:
            continue_bonus += 1
            value += continue_bonus
            # print("prev_genre_code: {}, entry[2]: {}, value: {}".format(
            #    prev_genre_code, entry[2], value))
        else:
            prev_genre_code = entry[2]
            continue_bonus = 0
        prev_block = entry[1]

    return value
