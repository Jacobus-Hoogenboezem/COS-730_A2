from submission_controller import SubmissionController

class UI:
    def __init__(self):
        self.controller = SubmissionController()
        
    # Step 2: UI receives submitResearchOutput(data) from Researcher
    #            UI -> SubmissionController : submit(data)
    def submitResearchOutput(self, data):
        print("[UI] Received submission from Researcher.")
        print("[UI] Forwarding to SubmissionController...")

        # Step 2: UI -> SubmissionController : submit(data)
        result = self.controller.submit(data) # void since ui only receives back if theres a error (WITH A CALL).

        if result == "error":
            print("[UI] Submission invalid. Returning error to Researcher. Displaying Invalid Submission")
            #Display invalid submission


    # def submit(self, submission, controller):
    #     print("[UI] Received submission from Researcher.")
    #     print("[UI] Forwarding to SubmissionController...")

    #     # Step 2: UI -> SubmissionController : submit(data)
    #     result = controller.submit(submission)

    #     # Step alt [invalid]: UI receives return error
    #     if result == "error":
    #         print("[UI] Submission invalid. Returning error to Researcher.")
    #         return "error"

    #     # Step final: UI displays outcome to Researcher
    #     print(f"[UI] Final outcome received: {result}")
    #     self.sendNotification(result)
    #     return result

    