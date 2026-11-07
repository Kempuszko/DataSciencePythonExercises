def calculate_risk_score(age: int, cholesterol: int, max_heart_rate: int) -> float:
    if age < 0 or cholesterol < 0 or max_heart_rate <= 0:
        raise ValueError('All parameters must be positive.')

    score = age * 0.2 + cholesterol * 0.05 - max_heart_rate * 0.03
    return round(score, 2)
