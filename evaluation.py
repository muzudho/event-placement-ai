def evaluate(pos_df):

    # 評価値
    value = 0

    # Block は A～F とする。
    # GenreCode は色々。
    block_dict = {}

    for _index, row in pos_df.iterrows():
        x = row["X"]
        y = row["Y"]
        block = row["BLOCK"]
        table_id = row["TABLE"]
        participant_id = row["PARTICIPANT"]
        genre_code = row["GENRE_CODE"]

        if not(block in block_dict):
            block_dict[block] = {}

        if not(genre_code in block_dict[block]):
            block_dict[block][genre_code] = 0

        block_dict[block][genre_code] += 1

    # 集計
    for block_name, genre_code_dict in block_dict.items():
        for genre_code_name, count in genre_code_dict.items():
            value += count ** 2
            break

    return value
