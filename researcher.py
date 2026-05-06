from ui import UI

class Researcher:
    def __init__(self):
        self.ui = UI()

    def initiateIntelligentSubmissionAndReviewSystem(self, data):
        print("[Researcher] Submitting research output...")
        
        # Step 1: Researcher -> UI : submitResearchOutput(self) 
        self.ui.submitResearchOutput(data) # call is void. result will come from Notification or display on UI if submission is invalid.

        # return  # outcome # Notification? Void?

    def sendNotification(self, notification):
        print(f"[Researcher] Received notification from notification_service: {notification}")
    