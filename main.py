# main.py

from feedback.feedback_entry import collect_feedback
from feedback.score_calculator import compute_average

if __name__ == "__main__":
    feedback_list = []

    while True:
        entry = collect_feedback()
        feedback_list.append(entry)

        cont = input("Add another? (y/n): ").lower()
        if cont != 'y':
            break

    average_score = compute_average([e.to_dict() for e in feedback_list])
    print(f"\nAverage score: {average_score:.2f}")
