class UI:
    def __init__(self, submission_controller):
        self.controller = submission_controller

    # Step 1: UI receives submitResearchOutput(data) from Researcher
    def submitResearchOutput(self, data):
        print("[UI] - submitResearchOutput(self, data) - Received submission from Researcher.")

        # Step 2: UI -> SubmissionController : submit(data)
        result = self.controller.submit(data)

        if result == "error":
            # alt [invalid]: validation failed
            print("[UI] - alt [invalid] - Displaying invalid submission message to Researcher.")

        elif result == "persistence_error":
            # alt [save failed]: database write failed 
            print("[UI] - alt [save failed] - Displaying persistence error to Researcher.")
