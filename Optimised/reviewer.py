class Reviewer:
    def __init__(self, data, evaluation_manager):
        self.id = data["ID"]
        self.name = data["name"]
        self.evaluation_manager = evaluation_manager

    def assignAndReview(self):
        print(f"[Reviewer] - assignAndReview(self) - Review assigned and conducted by {self.name}.")
        score = 7  # @TODO replace with real scoring logic
        print(f"[Reviewer] - Submitting score: {score}")
        self.evaluation_manager.submitScore(score)