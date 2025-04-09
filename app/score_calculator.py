
# score_calculator.py

def calculate_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def is_passing(score, threshold=5.0):
    return score >= threshold
