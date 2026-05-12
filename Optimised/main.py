from database import Database
from validator import Validator
from notification_service import NotificationService
from reviewer_manager import ReviewerManager
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
 
    # --- create and inject all objects ---
    researcher = Researcher()
    notification_service = NotificationService(researcher)  # inject researcher
    database = Database()
    evaluation_manager = EvaluationManager(database, notification_service)  # inject both
    submission_controller = SubmissionController(evaluation_manager)  # inject evaluation_manager
    ui = UI(submission_controller)  # inject controller
    researcher.set_ui(ui)  # late-bind UI into researcher to avoid cycle
 
    # --- Chain 1: Researcher initiates submission ---
    researcher.initiateIntelligentSubmissionAndReviewSystem(data)