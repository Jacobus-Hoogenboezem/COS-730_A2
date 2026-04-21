from submission_controller import SubmissionController
from ui import UI
from researcher import Researcher

if __name__ == "__main__":
    
    # Step 1: Researcher submits research output
    reseracher = Researcher()
    ui = UI()
    controller = SubmissionController()
    
    data = researcher.submitResearchOutput()
    
    # Step 2: UI Submit data to SubmissionController
    result = ui.submit(data, controller)

    print(f"\n[Main] Final outcome: {result}")