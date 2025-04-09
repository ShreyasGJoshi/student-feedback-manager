from feedback.score_calculator import calculate_average, is_passing

def test_calculate_average():
    scores = [7, 8, 9]
    assert calculate_average(scores) == 8

def test_is_passing_true():
    assert is_passing(6) == True

def test_is_passing_false():
    assert is_passing(4) == False
