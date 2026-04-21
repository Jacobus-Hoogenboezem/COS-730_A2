class ReviewerManager:
    def __init__(self, database):
        self.database = database

    # Step 6: ReviewerManager.getAvailableReviewers()
    def getAvailableReviewers(self):
        reviewerList = self.database.fetchReviewers()  # Step 7
        filtered = self.filterConflicts(reviewerList)  # Step 8
        filtered = self.checkWorkload(filtered)        # Step 9
        return filtered

    # Step 8: ReviewerManager.filterConflicts(reviewerList)
    def filterConflicts(self, reviewerList):
        return [r for r in reviewerList if 15 not in r["conflicts"]] # @TODO Add better checks.. check researcher IDs 

    # Step 9: ReviewerManager.checkWorkload(reviewerList)
    def checkWorkload(self, reviewerList):
        return [r for r in reviewerList if r["workload"] < 5] # @TODO Refine. How do we measure workload and what is too much?