class EvaluationManager:
    # Step 14: EvaluationManager.saveScore(score)
    def saveScore(self, score):
        self.scores = getattr(self, 'scores', [])
        self.scores.append(score)

    # Step 15: EvaluationManager.calculateAverage()
    def calculateAverage(self):
        return sum(self.scores) / len(self.scores)

    # Step 16: EvaluationManager.checkConsensus()
    def checkConsensus(self):
        avg = self.calculateAverage()
        return max(self.scores) - min(self.scores) <= 3

    # Step 17: EvaluationManager.applyRules()
    def applyRules(self):
        avg = self.calculateAverage()
        if avg >= 7:
            return "accepted"
        elif avg >= 4:
            return "revision"
        else:
            return "rejected"