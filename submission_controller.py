from validator import Validator
from database import Database
from reviewer_manager import ReviewerManager
from reviewer import Reviewer
from evaluation_manager import EvaluationManager
from notification_service import NotificationService
from database import Database

class SubmissionController:

    def __init__(self):
        self.validator = Validator()
        self.database = Database()
        self.reviewer_manager = ReviewerManager(self.database)
        self.evaluation_manager = EvaluationManager()
        self.notification_service = NotificationService()
        self.ui = UI()
        self.database = Database()
        self.reviewer = Reviewer()

    # Step 2: SubmissionController receives submit(data) from UI
    def submit(self, submission):
        print("[SubmissionController] Received submission.")

        # Step 3: SubmissionController -> Validator : validateFormat(data)
        print("[SubmissionController] Sending Validation Request to Validator")
        validation_result = self.validator.validateFormat(submission.to_dict())
        print(f"[SubmissionController] Validation result: {validation_result}")

        # Step alt [invalid]: return error to UI
        if validation_result == "invalid":
            print("[SubmissionController] Validation failed. Returning error to UI (as a call).")
            return "error"

        # # Step [valid] continues:

        # Step 5: SubmissionController -> Database : saveSubmission(data)
        confirmation = self.database.saveSubmission(submission.to_dict())
        print(f"[SubmissionController] Database confirmation: {confirmation}")

        # Step 6: SubmissionController -> ReviewerManager : getAvailableReviewers()
        filtered_reviewers = self.reviewer_manager.getAvailableReviewers()
        print(f"[SubmissionController] Received filtered reviewers: {[r['name'] for r in filtered_reviewers]}")

        # Step loop [assign reviewers]:
        # SubmissionController -> Reviewer : assignReview() for each reviewer
        # reviewer_objects = []
        for r_data in filtered_reviewers:
            self.reviewer = Reviewer(r_data)
            self.reviewer.assignReview()   # Step 11
            # reviewer_objects.append(reviewer)

        # Step 12: SubmissionController -> EvaluationManager : startEvaluation()
        self.evaluation_manager.startEvaluation()

        # # Step alt [accepted / rejected / revision]:
        # # NotificationService called by EvaluationManager in baseline diagram
        # if outcome == "accepted":
        #     self.notification_service.notifyAcceptance()
        # elif outcome == "rejected":
        #     self.notification_service.notifyRejection()
        # else:
        #     self.notification_service.notifyRevision()

        # return outcome