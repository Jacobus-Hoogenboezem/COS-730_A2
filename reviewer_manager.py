from database import Database

class ReviewerManager:
    def __init__(self, database):
        self.database = Database()

    # Step 6: ReviewerManager.getAvailableReviewers()
    def getAvailableReviewers(self):
        print("[ReviewerManager] received filter request from SubmissionController")
        reviewerList = self.database.fetchReviewers()  # Step 7
        print("[ReviewerManager] Received reviewer lisst from Database")
        filtered = self.filterConflicts(reviewerList)  # Step 8
        print("[ReviewerManager] filtered Conflits")
        filtered = self.checkWorkload(filtered)        # Step 9
        print("[ReviewerManager] filtered Workloads")
        print("[ReviewerManager] returning available reviewers to SubmissionController")
        return filtered

    # Step 8: ReviewerManager.filterConflicts(reviewerList)
    def filterConflicts(self, reviewerList):
        return [r for r in reviewerList if 15 not in r["conflicts"]] # @TODO Add better checks.. check researcher IDs 

    # Step 9: ReviewerManager.checkWorkload(reviewerList)
    def checkWorkload(self, reviewerList):
        return [r for r in reviewerList if r["workload"] < 5] # @TODO Refine. How do we measure workload and what is too much?

    def submitScore(self, score):
        print("[ReviewerManager] Received submit score request")
        self.database.saveScore(score)

