import pandas as pd

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def new_mappings(par_id_list, flo_id_list):
    # print("Info    : my_lib/mapper/new_mappings().")

    # print("par_id_list: {}".format(par_id_list))
    # print("Info    : len(par_id_list) : {}".format(len(par_id_list)))

    # print("flo_id_list: {}".format(flo_id_list))
    # print("Info    : len(flo_id_list) : {}".format(len(flo_id_list)))
    """
    Make: mappings.csv
    ------------------

    PARTICIPANT,TABLE
    57,25
    38,26
    6,8
    """
    df = pd.DataFrame(columns=['TABLE', 'PARTICIPANT'])

    for i, table_id in enumerate(flo_id_list):
        if i < len(par_id_list):
            participants_id = par_id_list[i]
        else:
            participants_id = 0

        new_row = pd.DataFrame(
            [table_id, participants_id], index=df.columns).T
        df = df.append(new_row)

    return df
