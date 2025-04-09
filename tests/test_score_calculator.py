import pytest
from feedback.score_calculator import calculate_average, is_passing

def test_calculate_average():
    assert calculate_average([5, 7, 9]) == 7.0

def test_average_empty_list():
    assert calculate_average([]) == 0

def test_is_passing_true():
    assert is_passing(6) is True

def test_is_passing_false():
    assert is_passing(4.5) is False

def test_is_passing_custom_threshold():
    assert is_passing(6, threshold=6) is True
    assert is_passing(5.9, threshold=6) is False

