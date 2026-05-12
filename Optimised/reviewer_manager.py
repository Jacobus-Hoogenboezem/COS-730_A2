class ReviewerManager:
    def __init__(self, database):
        self.database = database   # FIX: use the injected instance, not a new one

    # Step 6: ReviewerManager.getAvailableReviewers()
    def getAvailableReviewers(self):
        print("[ReviewerManager] - getAvailableReviewers(self) - Fetching and filtering reviewers.")
        reviewer_list = self.database.fetchReviewers()

        filtered = self._filterConflicts(reviewer_list)
        filtered = self._checkWorkload(filtered)

        print(f"[ReviewerManager] - Returning {len(filtered)} eligible reviewer(s).")
        return filtered

    # Private: not part of the public interface / SD messages
    def _filterConflicts(self, reviewer_list):
        print("[ReviewerManager] - _filterConflicts() - Removing conflicted reviewers.")
        return [r for r in reviewer_list if 15 not in r["conflicts"]]  # @TODO Add better checks.. check researcher IDs 

    # Private: not part of the public interface / SD messages
    def _checkWorkload(self, reviewer_list):
        print("[ReviewerManager] - _checkWorkload() - Removing overloaded reviewers.")
        return [r for r in reviewer_list if r["workload"] < 5]  # @TODO Refine. How do we measure workload and what is too much?