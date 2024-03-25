from load_data import load_data, COLUMNS_CHECK
from load_model import load_model
from aggregate_result import aggregate_result
import json

if __name__ == "__main__":
    PATH = "src/main/predictions/predictions.json"
    data = load_data()
    prediction = load_model().predict(data[COLUMNS_CHECK])
    final_df = aggregate_result(data, prediction)
    final_df.to_json(PATH, orient="records")
    with open(PATH, "r") as file:
        print(json.load(file))
