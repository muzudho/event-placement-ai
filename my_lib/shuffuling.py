import random

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def go_shuffule(pd_list, fl_list):

    # Location.
    output_mappings = "./event-placement-ai/auto-generated/mappings.csv"

    random.shuffle(pd_list)
    # print("pd_list: {}".format(pd_list))

    random.shuffle(fl_list)
    # print("fl_list: {}".format(fl_list))

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
        for i in range(len(pd_list)):
            file.write(
                "{},{}\n".format(pd_list[i], fl_list[i])
            )
    except Exception as e:
        print(e)
    finally:
        file.close()
