class EvaluationManager:
    def __init__(self, database, notification_service, outcome_policy):
        self.database = database
        self.notification_service = notification_service
        self.outcome_policy = outcome_policy
        self.scores = []

    # Score collection (called once per reviewer inside the unified loop)

    def submitScore(self, score):
        print(f"[EvaluationManager] - submitScore(self, score={score}) - Score received and stored.")
        self.scores.append(score)
        self.database.saveScore(score) 
    def startEvaluation(self):
        print("[EvaluationManager] - startEvaluation(self) - All scores received. Starting evaluation.")

        avg       = self.calculateAverage()
        consensus = self.checkConsensus()

        # consensus result is now consumed by OutcomePolicy
        # (previously it was computed and silently discarded. dead logic).
        outcome = self.outcome_policy.determineOutcome(avg, consensus)

        # notification based on outcome
        if outcome == "accepted":
            self.notification_service.notifyAcceptance()
        elif outcome == "revision":
            self.notification_service.notifyRevision()
        else:
            self.notification_service.notifyRejection()

    def calculateAverage(self):
        print("[EvaluationManager] - calculateAverage(self) - Calculating average score.")
        avg = sum(self.scores) / len(self.scores)
        print(f"[EvaluationManager] - Average score: {avg:.2f}")
        return avg

    def checkConsensus(self):
        print("[EvaluationManager] - checkConsensus(self) - Checking reviewer consensus.")
        consensus = (max(self.scores) - min(self.scores)) <= 3
        print(f"[EvaluationManager] - Consensus reached: {consensus}")
        return consensus