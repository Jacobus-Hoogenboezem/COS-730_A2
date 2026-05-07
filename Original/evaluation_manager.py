class EvaluationManager:
    def __init__(self, database, notification_service):
        self.database = database
        self.notification_service = notification_service
        self.scores = []

    # Step 13: EvaluationManager.startEvaluation()
    def startEvaluation(self):
        print("[EvaluationManager] - startEvaluation(self) - Evaluation started.")

    # Step 13: Reviewer -> EvaluationManager : submitScore(score)
    def submitScore(self, score): 
        print("[EvaluationManager] - submitScore(self, score) - Received request to submit score.")
        self.scores.append(score)
        self.database.saveScore(score)
 
 
        avg = self.calculateAverage()

        self.checkConsensus()

        res = self.applyRules()
        if res == "accepted":
            self.notification_service.notifyAcceptance()
        elif res == "revision":
            self.notification_service.notifyRevision()
        else:
            self.notification_service.notifyRejection()

    # Step 15: EvaluationManager.calculateAverage()
    def calculateAverage(self):
        print("[EvaluationManager] - calculateAverage(self) - Received request to calculate average.")
        return sum(self.scores) / len(self.scores)

    # Step 16: EvaluationManager.checkConsensus()
    def checkConsensus(self):
        print("[EvaluationManager] - checkConsensus(self) - Received request to check Consensus.")
        return max(self.scores) - min(self.scores) <= 3

    # Step 17: EvaluationManager.applyRules()
    def applyRules(self):
        print("[EvaluationManager] - applyRules(self) - Received request to apply rules.")
        avg = self.calculateAverage()
        if avg >= 7:
            return "accepted"
        elif avg >= 4:
            return "revision"
        else:
            return "rejected"