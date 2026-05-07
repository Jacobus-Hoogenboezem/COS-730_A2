class EvaluationManager:
    def __init__(self, database, notification_service):
        self.database = database
        self.notification_service = notification_service
        self.scores = []

    # Step 13: EvaluationManager.startEvaluation()
    def startEvaluation(self):
        print("[EvaluationManager] Evaluation started.")

    # Step 13: Reviewer -> EvaluationManager : submitScore(score)
    def submitScore(self, score): 
        print("[EvaluationManager] Received request to submit score.")
        self.scores.append(score)
        self.database.saveScore(score)
        print("[EvaluationManager] Calling database.saveScore()")
 
 
        print("[EvaluationManager] Calling calculateAverage()")
        avg = self.calculateAverage()

        print("[EvaluationManager] Calling checkConsensus()")
        self.checkConsensus()

        # Step 17: notify based on average score
        if avg >= 7:
            print("[EvaluationManager] Calling notification_service.notifyAcceptance()")
            self.notification_service.notifyAcceptance()
        elif avg >= 4:
            print("[EvaluationManager] Calling notification_service.notifyRevision()")
            self.notification_service.notifyRevision()
        else:
            print("[EvaluationManager] Calling notification_service.notifyRejection()")
            self.notification_service.notifyRejection()

    # Step 15: EvaluationManager.calculateAverage()
    def calculateAverage(self):
        return sum(self.scores) / len(self.scores)

    # Step 16: EvaluationManager.checkConsensus()
    def checkConsensus(self):
        return max(self.scores) - min(self.scores) <= 3