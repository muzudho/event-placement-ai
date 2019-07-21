"""
Note.
    Root directory: Visual studio code workspace root.
"""


def write_mappings(par_id_list, flo_id_list):
    print("Info    : my_lib/mapper/write_mappings().")

    # Location.
    output_mappings = "./event-placement-ai/auto-generated/mappings.csv"

    # print("par_id_list: {}".format(par_id_list))
    print("Info    : len(par_id_list) : {}".format(len(par_id_list)))

    # print("flo_id_list: {}".format(flo_id_list))
    print("Info    : len(flo_id_list) : {}".format(len(flo_id_list)))

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

        file.write("TABLE,PARTICIPANT\n")
        for i, table_id in enumerate(flo_id_list):
            if i < len(par_id_list):
                participants_id = par_id_list[i]
            else:
                participants_id = 0

            file.write(
                "{},{}\n".format(table_id, participants_id)
            )
    except Exception as e:
        print(e)
    finally:
        file.close()
