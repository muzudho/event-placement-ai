import pandas as pd

#
# Note.
#
# Root directory: Visual studio code workspace root.
#


def convert_floor_map(input_block_file, input_table_file):
    # print("Info    : biuld_floor_map/convet_floor_map().")

    try:
        bl_file = open(input_block_file)
        try:
            ta_file = open(input_table_file)

            id_column = []
            x_column = []
            y_column = []
            block_column = []

            bl_lines = bl_file.readlines()
            for y, line in enumerate(bl_lines):
                for x, block in enumerate(line):
                    if block != '.' and block != '\n':
                        x_column.append(x)
                        y_column.append(y)
                        block_column.append(block)

            ta_lines = ta_file.readlines()
            for row in ta_lines:
                cols = row.split(",")
                for x, number_text in enumerate(cols):
                    num = int(number_text)
                    if num != 0:
                        id_column.append(num)

            # 机の個数をベースで。
            # print("len(id_column   ):{}".format(len(id_column)))
            # print("len(x_column    ):{}".format(len(x_column)))
            # print("len(y_column    ):{}".format(len(y_column)))
            # print("len(block_column):{}".format(len(block_column)))

            df = pd.DataFrame(columns=['ID', 'X', 'Y', 'BLOCK'])

            for i, block in enumerate(block_column):
                # print("i:{}".format(i))

                new_row = pd.DataFrame(
                    [id_column[i], x_column[i], y_column[i], block], index=df.columns).T
                df = df.append(new_row)

            return df

        except Exception as e:
            print(e)
        finally:
            ta_file.close()
    except Exception as e:
        print(e)
    finally:
        bl_file.close()
