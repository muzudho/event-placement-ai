#
# Note.
#
# Root directory: Visual studio code workspace root.
#
block_input_file = "./event-placement-ai/input-data/floor-map-block.txt"
table_input_file = "./event-placement-ai/input-data/floor-map-table-number.txt"
output_file_name = "./event-placement-ai/auto-generated/floor-map.csv"


def convert_map():
    try:
        bl_file = open(block_input_file)
        try:
            ta_file = open(table_input_file)

            try:
                out_file = open(output_file_name, 'w', encoding='utf-8')

                # Column name, No space.
                out_file.write("ID,X,Y,BLOCK\n")
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
                print("len(id_column   ):{}".format(len(id_column)))
                print("len(x_column    ):{}".format(len(x_column)))
                print("len(y_column    ):{}".format(len(y_column)))
                print("len(block_column):{}".format(len(block_column)))
                for i, block in enumerate(block_column):
                    # print("i:{}".format(i))
                    out_file.write("{},{},{},{}\n".format(
                        id_column[i], x_column[i], y_column[i], block))

            except Exception as e:
                print(e)
            finally:
                out_file.close()

        except Exception as e:
            print(e)
        finally:
            ta_file.close()
    except Exception as e:
        print(e)
    finally:
        bl_file.close()


convert_map()
print("Info    : Finished.")
