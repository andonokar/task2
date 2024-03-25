import joblib


def load_model():
    """
    Function that loads the model trained in pkl located in resources folder
    :return: The trained Linear Regression model
    """
    linear_regression = joblib.load(f"src/main/resources/linear_regression_model.pkl")
    return linear_regression
