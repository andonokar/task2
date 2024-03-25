import pandas as pd
from src.main.aggregate_result import aggregate_result


def test_aggregate_result():
    df = pd.read_json("src/test/resources/correct.json")
    final_df = aggregate_result(df, [1])
    columns = list(df.columns)
    columns.append("predicted_revenue")
    assert all(column in final_df for column in columns)
