import pandas as pd


def new_json(pos_df, test_number, variation_number, max_value):
    # Location.
    json_file = "./event-placement-ai/auto-generated/placement-{}-{}.json"

    try:
        file = open(json_file.format(
            test_number, variation_number), 'w', encoding='utf-8')
        file.write(
            """
{{
    "maxValue" : {0}
}}
            """.format(max_value)
        )
    except Exception as e:
        print(e)
    finally:
        file.close()
