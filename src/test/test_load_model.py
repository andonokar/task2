from src.main.load_model import load_model
import pickle
import joblib
from sklearn.linear_model import LinearRegression


def test_load_model(monkeypatch):
    model = load_model()
    print(type(model))
    assert isinstance(model, LinearRegression)
