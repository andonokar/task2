from src.main.load_data import load_data, COLUMNS_CHECK
import pytest


def test_load_data_key_error(monkeypatch):
    with pytest.raises(KeyError):
        monkeypatch.setenv("DATA_PATH", "src/test/resources/key_error.json")
        load_data()


def test_load_data_not_json(monkeypatch):
    with pytest.raises(NotImplementedError):
        monkeypatch.setenv("DATA_PATH", "src/test/resources/test.csv")
        load_data()


def test_load_data(monkeypatch):
    monkeypatch.setenv("DATA_PATH", "src/test/resources/correct.json")
    df = load_data()
    assert all(column in df.columns for column in COLUMNS_CHECK)
