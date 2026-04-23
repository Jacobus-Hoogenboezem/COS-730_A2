class Reviewer:
    def __init__(self, data):
        self.id = data["ID"]
        self.name = data["name"]

    # Step 11: Reviewer.assignReview()
    def assignReview(self):
        return f"Review assigned to {self.name}"

    # Step 13: Reviewer.submitScore(score) 
    def submitScore(self, score):
        return score