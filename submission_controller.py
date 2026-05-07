from validator import Validator
from database import Database
from reviewer_manager import ReviewerManager
from reviewer import Reviewer

class SubmissionController:

    def __init__(self, evaluation_manager):
        self.validator = Validator()
        self.database = Database()
        self.reviewer_manager = ReviewerManager(self.database)
        self.evaluation_manager = evaluation_manager  

    # Step 2: SubmissionController receives submit(data) from UI
    def submit(self, submission):
        print("[SubmissionController] Received submission.")

        # Step 3: SubmissionController -> Validator : validateFormat(data)
        print("[SubmissionController] Sending validation request to Validator.")
        validation_result = self.validator.validateFormat(submission.to_dict())
        print(f"[SubmissionController] Validation result: {validation_result}")

        # Step alt [invalid]: return error to UI
        if validation_result == "invalid":
            print("[SubmissionController] Validation failed. Returning error to UI.")
            return "error"

        # Step 5: SubmissionController -> Database : saveSubmission(data)
        confirmation = self.database.saveSubmission(submission.to_dict())
        print(f"[SubmissionController] Database confirmation: {confirmation}")

        # Step 6: SubmissionController -> ReviewerManager : getAvailableReviewers()
        filtered_reviewers = self.reviewer_manager.getAvailableReviewers()
        print(f"[SubmissionController] Received filtered reviewers: {[r['name'] for r in filtered_reviewers]}")

        # Step loop [assign reviewers]:
        # SubmissionController -> Reviewer : assignReview() for each reviewer
        for r_data in filtered_reviewers:
            reviewer = Reviewer(r_data, self.evaluation_manager)
            reviewer.assignReview()  # Step 11

        # Step 12: SubmissionController -> EvaluationManager : startEvaluation()
        self.evaluation_manager.startEvaluation()