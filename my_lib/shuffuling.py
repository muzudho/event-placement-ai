import random

"""
Note.
    Root directory: Visual studio code workspace root.
"""


def go_shuffule(pd_list, fl_list):
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
        output_mappings = "./event-placement-ai/html_generator/auto-generated/mappings.csv"
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
