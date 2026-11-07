import pytest
from risk_score import calculate_risk_score


def test_calculate_risk_score_returns_float():
    result = calculate_risk_score(50, 200, 150)
    assert isinstance(result, float)


def test_calculate_risk_score_expected_value():
    assert calculate_risk_score(52, 240, 150) == 18.9


def test_calculate_risk_score_invalid_age():
    with pytest.raises(ValueError):
        calculate_risk_score(-1, 240, 150)
