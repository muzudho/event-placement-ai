import pandas as pd


def write_json(test_number, variation_number, progress_num, json):
    # Location.
    json_file = "./event-placement-ai/auto-generated/placement-{}-{}-{}.json"

    try:
        file = open(json_file.format(
            test_number, variation_number, progress_num), 'w', encoding='utf-8')

        file.write(json)
    except Exception as e:
        print(e)
    finally:
        file.close()
    return


def new_json(test_number, variation_number, progress_num, value):
    return """
{{
    "test" : {0},
    "variation" : {1},
    "progress" : {2},
    "value" : {3}
}}
            """.format(test_number, variation_number, progress_num, value)
