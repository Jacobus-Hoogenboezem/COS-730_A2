from database import Database
from validator import Validator
from notification_service import NotificationService
from reviewer_manager import ReviewerManager
from outcome_policy import OutcomePolicy
from evaluation_manager import EvaluationManager
from submission_controller import SubmissionController
from ui import UI
from researcher import Researcher
from shared_objects import Submission

if __name__ == "__main__":

    # Dummy submission data for researcher to use.
    data = Submission(
        title="Differential Evolution for image registration",
        content="A software system grounded on Differential Evolution to automatically...",
        researcher_id=15
    )

    # --- Wire all objects via dependency injection (no circular imports) ---
    researcher          = Researcher()
    notification_service = NotificationService(researcher)
    database            = Database()
    outcome_policy      = OutcomePolicy()
    evaluation_manager  = EvaluationManager(database, notification_service, outcome_policy)
    reviewer_manager    = ReviewerManager(database)
    submission_controller = SubmissionController(evaluation_manager, reviewer_manager)
    ui                  = UI(submission_controller)
    researcher.set_ui(ui)

    # --- Researcher initiates the submission pipeline ---
    researcher.initiateIntelligentSubmissionAndReviewSystem(data)