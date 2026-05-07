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

    researcher = Researcher()
    researcher.initiateIntelligentSubmissionAndReviewSystem(data)

    # independent initiator
    
