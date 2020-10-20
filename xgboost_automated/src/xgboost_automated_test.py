from . import xgboost_automated

def test_xgboost_automated():
    assert xgboost_automated.apply("Jane") == "hello Jane"
