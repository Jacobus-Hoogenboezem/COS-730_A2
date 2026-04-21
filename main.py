from submission_controller import SubmissionController
from ui import UI
from researcher import Researcher

if __name__ == "__main__":
    
    researcher = Researcher()
    ui = UI()
    controller = SubmissionController()
    
    # Step 1: Researcher submits research output to UI
    submission = researcher.submitResearchOutput()
    outcome = ui.submit(submission, controller)

    print(f"\n[Main] Final outcome: {outcome}")