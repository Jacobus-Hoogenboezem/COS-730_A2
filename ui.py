class UI:

    # Step 2: UI receives submitResearchOutput(data) from Researcher
    #            UI -> SubmissionController : submit(data)
    def submit(self, submission, controller):
        print("[UI] Received submission from Researcher.")
        print("[UI] Forwarding to SubmissionController...")

        # Step 2: UI -> SubmissionController : submit(data)
        result = controller.submit(submission)

        # Step alt [invalid]: UI receives return error
        if result == "error":
            print("[UI] Submission invalid. Returning error to Researcher.")
            return "error"

        # Step final: UI displays outcome to Researcher
        print(f"[UI] Final outcome received: {result}")
        self.sendNotification(result)
        return result

    # Step last: UI -> Researcher : sendNotification()
    def sendNotification(self, outcome):
        print(f"[UI] Sending notification to Researcher: {outcome}")