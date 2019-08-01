"""
テーブルを配置換えする操作。
"""

import random


def swap_participant(index1, index2, position):
    """
    テーブルＩＤは固定し、参加者ＩＤを入れ替えます。
    """
    temp_par_id = position.par_id_list[index1]
    temp_genre_code = position.genre_code_list[index1]

    position.par_id_list[index1] = position.par_id_list[index2]
    position.genre_code_list[index1] = position.genre_code_list[index2]

    position.par_id_list[index2] = temp_par_id
    position.genre_code_list[index2] = temp_genre_code
    return


def shift_smaller(position):
    """
    ブロック単位で１つシフトします。[1,2,3,4]を、[2,3,4,1]にする動きです。
    """

    prev_block = None
    # テーブルID順に並んでいるとします。
    for index, block in enumerate(position.block_list):
        # for index, row in floor_df.iterrows():
        if prev_block == block:
            swap_participant(
                index-1, index, position)

        prev_block = block

    return


def shift_bigger(position):
    """
    ブロック単位で１つシフトします。[1,2,3,4]を、[4, 1, 2, 3]にする動きです。
    """

    prev_block = None
    index = len(position.block_list)-1
    # テーブルID順に並んでいるとします。
    for block in reversed(position.block_list):
        # print("shift_bigger: index={}, block={}.".format(index, block))
        if prev_block == block:
            swap_participant(
                index, index+1, position)

        prev_block = block
        index -= 1

    return


def for_block_asc(position, callback_head_block, callback_same_block):
    """
    ブロックの切れ目が分かるループです。昇順。
    """
    # テーブルID順に並んでいるとします。
    prev_block = None
    for i in range(0, len(position.block_list)):
        if prev_block == position.block_list[i]:
            callback_same_block(i, position.block_list[i])
        else:
            callback_head_block(i, position.block_list[i])
        prev_block = position.block_list[i]
    return


def for_block_desc(position, callback_tail_block, callback_same_block):
    """
    ブロックの切れ目が分かるループです。降順。
    """
    # テーブルID順に並んでいるとします。
    prev_block = None
    for i in reversed(range(0, len(position.block_list))):
        if prev_block == position.block_list[i]:
            callback_same_block(i, position.block_list[i])
        else:
            callback_tail_block(i, position.block_list[i])
        prev_block = position.block_list[i]
    return


def pick_up_index_list(position):
    """
    index_list = []
    for i in range(0, len(position.par_id_list)):
        index_list.append(i)
    return index_list
    """

    order_list = [0] * len(position.tbl_id_list)
    index = 0
    for tbl_id in position.tbl_id_list:
        order_list[tbl_id-1] = index
        index += 1

    # print("order_list: {}".format(order_list))

    index_list = []
    prev_genre_code = None
    prev_index = -1
    # 同じジャンルコードが連続しているところは、始点と終点だけを取る。
    for index in order_list:
        genre_code = position.genre_code_list[index]

        # print("prev_genre_code: {}, genre_code: {}".format(
        #    prev_genre_code, genre_code))
        if prev_genre_code == None:
            prev_genre_code = genre_code

            # Index of start.
            index_list.append(index)

        elif prev_genre_code != genre_code:
            prev_genre_code = genre_code
            # print("start: {}, end: {}".format(
            #    start, current-1))

            if index_list[len(index_list)-1] != prev_index:
                # Index of previous end.
                index_list.append(prev_index)

            # Index of start.
            index_list.append(index)

        prev_index = index

    # print("len(genre_code_list)-1: {}".format(len(position.genre_code_list)-1))
    index_list.append(order_list[len(order_list)-1])
    # print("index_list: {}".format(index_list))

    # # 並び順を崩さないようにすること。
    # # result = list(set(index_list))
    # # print("result: {}".format(result))
    return index_list


def choice_index(position):
    # Pick up table.
    picked_up_index_list = pick_up_index_list(position)
    # print("picked_up_index_list: {}".format(picked_up_index_list))

    # リトライ回数が多すぎると、終わりたいときに、逆に終わらないかもしれない。
    choice_retry = 3
    genre_code1 = None
    genre_code2 = None
    while genre_code1 == genre_code2 and 0 < choice_retry:
        # Random choice at first.
        size = len(picked_up_index_list)
        index11 = random.randint(0, size-1)
        index1 = picked_up_index_list[index11]
        genre_code1 = position.genre_code_list[index1]

        # 同じ色はなるべく選ばない。
        index12 = random.randint(0, size-1)
        index2 = picked_up_index_list[index12]
        genre_code2 = position.genre_code_list[index2]
        choice_retry -= 1

    # print("size={}, index1={}, index2={}".format(size, index1, index2))
    # print("Choiced index1={}, index2={}".format(index1, index2))
    return index1, index2


def count_joined_genre_code(position):
    """
    TODO 同じブロック内での、連続するジャンルコードの数。
    """

    result_dict = {}
    prev_block = None
    prev_genre_code = None
    count = 0

    def head(index, block, prev_block, prev_genre_code, count):
        """
        Head.
        """
        result_dict[prev_block] = count
        prev_block = block
        prev_genre_code = position.genre_code_list[index]
        count = 0

    def same(index, block, prev_genre_code):
        """
        Same.
        """
        genre_code = position.genre_code_list[index]
        if prev_genre_code != genre_code:
            result_dict[block] = count
            count = 0
        prev_genre_code = genre_code
        count += 1

    for_block_asc(
        position,
        lambda index, block: head(
            index, block, prev_block, prev_genre_code, count),
        lambda index, block: same(index, block, prev_genre_code)
    )

    return result_dict
