class UI:
    def __init__(self, submission_controller):
        self.controller = submission_controller
 
    # Step 2: UI receives submitResearchOutput(data) from Researcher
    #         UI -> SubmissionController : submit(data)
    def submitResearchOutput(self, data):
        print("[UI] - submitResearchOutput(self, data) - Received submission from Researcher.")
 
        # Step 2: UI -> SubmissionController : submit(data)
        result = self.controller.submit(data)  # void unless invalid
 
        if result == "error":
            print("[UI] - return error - Submission invalid. Displaying error to Researcher.")