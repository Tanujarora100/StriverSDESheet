from typing import List
from queue import PriorityQueue

class Pair:
    def __init__(self, points, student_id):
        # Initialize the points attribute with the value passed in as a parameter
        self.points = points
        # Initialize the student_id attribute with the value passed in as a parameter
        self.student_id = student_id

    def __lt__(self, other):
        if self.points == other.points:
            return self.student_id < other.student_id
        return self.points > other.points

    def __str__(self):
        return f"Pair{{'points': {self.points}, 'student_id': {self.student_id}}}"

def top_students(positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
    ans = []
    positive_set = set(positive_feedback)
    negative_set = set(negative_feedback)
    pq = PriorityQueue()

    for i in range(len(report)):
        word_array = report[i].split()
        points = 0
        for word in word_array:
            if word in positive_set:
                points += 3
            elif word in negative_set:
                points -= 1

        student_id_value = student_id[i]
        pq.put(Pair(points, student_id_value))

    while k > 0 and not pq.empty():
        p = pq.get()
        ans.append(p.student_id)
        k -= 1

    return ans

# Example usage:
positive_feedback = ["good", "excellent", "outstanding"]
negative_feedback = ["poor", "bad", "horrible"]
report = ["good excellent", "poor bad horrible", "good good good"]
student_id = [1, 2, 3]
k = 2
result = top_students(positive_feedback, negative_feedback, report, student_id, k)
print(result)
