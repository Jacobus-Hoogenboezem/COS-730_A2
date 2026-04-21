from submission_controller import SubmissionController
from ui import UI
from researcher import Researcher

if __name__ == "__main__":
    
    reseracher = Researcher()
    ui = UI()
    controller = SubmissionController()
    
    # Step 1: Researcher submits research output
    submission = researcher.submitResearchOutput()
    
    # Step 2: UI Submit data to SubmissionController
    outcome = ui.submit(data, controller)

    print(f"\n[Main] Final outcome: {outcome}")