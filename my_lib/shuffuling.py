import random

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def go_shuffule(par_id_list, flo_id_list):

    # Location.
    output_mappings = "./event-placement-ai/auto-generated/mappings.csv"

    random.shuffle(par_id_list)
    # print("par_id_list: {}".format(par_id_list))

    random.shuffle(flo_id_list)
    # print("flo_id_list: {}".format(flo_id_list))

    """
    Make: mappings.csv
    ------------------

    PARTICIPANT,TABLE
    57,25
    38,26
    6,8
    """
    try:
        file = open(output_mappings, 'w', encoding='utf-8')

        file.write("PARTICIPANT,TABLE\n")
        for i in range(len(par_id_list)):
            file.write(
                "{},{}\n".format(par_id_list[i], flo_id_list[i])
            )
    except Exception as e:
        print(e)
    finally:
        file.close()
