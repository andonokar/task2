import pandas as pd
import os

COLUMNS_CHECK = ["total_impressions", "viewable_impressions", "measurable_impressions"]


def load_data() -> pd.DataFrame:
    """
    Function that gets the environment variable DATA_PATH and load the data into a pandas
    dataframe, or defaults to a json file in resources folder
    dataframe must have all the 3 README columns, otherwise will raise an error
    :return: a pandas dataframe with json_data
    """
    json_path = os.environ.get("DATA_PATH", f"src/main/resources/AD-Tech.json")
    if not json_path.endswith(".json"):
        raise NotImplementedError("File must be an json format")
    df_json = pd.read_json(json_path, orient="records")
    if not all(column in df_json for column in COLUMNS_CHECK):
        raise KeyError(f"Keys in {COLUMNS_CHECK} are missing")
    return df_json
