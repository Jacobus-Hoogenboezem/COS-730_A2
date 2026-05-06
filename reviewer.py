from evaluation_manager import EvaluationManager

class Reviewer:
    def __init__(self, data):
        self.id = data["ID"]
        self.name = data["name"]
        self.reviewers = [
            {"ID": 1, "name": "Reviewer 1", "workload": 2, "conflicts": []},
            {"ID": 2, "name": "Reviewer 2", "workload": 5, "conflicts": []},
            {"ID": 3, "name": "Reviewer 3", "workload": 1, "conflicts": [15]},
        ]
        self.evaluation_manager = EvaluationManager()

    # Step 11: Reviewer.assignReview()
    def assignReview(self):
        return f"Review assigned to {self.name}"

    def what(self):
        for reviewer in self.reviewers:
            score = 1 # calculate scores, maybe random?
            self.evaluation_manager.submitScore(score)
