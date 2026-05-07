class Reviewer:
    def __init__(self, data, evaluation_manager):
        self.id = data["ID"]
        self.name = data["name"]
        self.evaluation_manager = evaluation_manager
 
    # Step 11: Reviewer.assignReview()
    def assignReview(self):
        print(f"[Reviewer] - assignReview(self) - Review assigned to {self.name}.")
        score = 7 # @TODO place holder score
        self.evaluation_manager.submitScore(score)
 