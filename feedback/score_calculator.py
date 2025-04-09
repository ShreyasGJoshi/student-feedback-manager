# feedback/score_calculator.py

def compute_average(feedback_dicts):
    if not feedback_dicts:
        return 0.0
    total = sum(entry["score"] for entry in feedback_dicts)
    return total / len(feedback_dicts)
