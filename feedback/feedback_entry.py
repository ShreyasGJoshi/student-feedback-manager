# feedback_entry.py

class FeedbackEntry:
    def __init__(self, student_name, score, comments):
        self.student_name = student_name
        self.score = score
        self.comments = comments

    def to_dict(self):
        return {
            "name": self.student_name,
            "score": self.score,
            "comments": self.comments
        }

def collect_feedback():
    name = input("Enter student name: ")
    score = float(input("Enter score (0 to 10): "))
    comments = input("Enter comments: ")
    entry = FeedbackEntry(name, score, comments)
    return entry

