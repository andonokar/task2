import pandas as pd


def aggregate_result(dataframe, prediction) -> pd.DataFrame:
    return pd.concat(
        [dataframe, pd.DataFrame(prediction, columns=["predicted_revenue"])], axis=1)
