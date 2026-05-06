from database import Database
from notification_service import NotificationService
from researcher import Researcher

class EvaluationManager:
    def __init__(self):
        self.database = Database()
        self.notification_service = NotificationService()

    # Step 13: EvaluationManager.startEvaluation()
    def startEvaluation(self):
        # ??
        return 

    # Step 13: Reviewer.submitScore(score) 
    def submitScore(self, score):
        print("[EvaluationManager] Received request to submit score")
        self.database.saveScore()
        print("[EvaluationManager] Calling database.saveScore()")
        # elf.scores = getattr(self, 'scores', [])
        # self.scores.append(score)
        
        print("[EvaluationManager] Calling calculateAverage()")
        avg = self.calculateAverage()

        print("[EvaluationManager] Calling checkConsensus()")
        cnss = self.checkConsensus()

        # Step 17: 
        if avg >= 7:
            print("[EvaluationManager] Calling notification_service.notifyAcceptance()")
            self.notification_service.notifyAcceptance()
        elif avg >= 4:
            print("[EvaluationManager] Calling notification_service.notifyRevision()")
            self.notification_service.notifyRevision()
        else:
            print("[EvaluationManager] Calling notification_service.notifyRejection()")
            self.notification_service.notifyRejection()
    
    # # Step 14: EvaluationManager.saveScore(score)
    # def saveScore(self, score):
    #     self.scores = getattr(self, 'scores', [])
    #     self.scores.append(score)

    # Step 15: EvaluationManager.calculateAverage()
    def calculateAverage(self):
        return sum(self.scores) / len(self.scores)

    # Step 16: EvaluationManager.checkConsensus()
    def checkConsensus(self):
        # avg = self.calculateAverage()
        return max(self.scores) - min(self.scores) <= 3
