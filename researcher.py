
class Researcher:
    def __init__(self):
        self.ui = None

    def set_ui(self, ui):
        self.ui = ui
 
    def initiateIntelligentSubmissionAndReviewSystem(self, data):
        print("[Researcher] Submitting research output...")
 
        # Step 1: Researcher -> UI : submitResearchOutput(data)
        self.ui.submitResearchOutput(data)  # void — result comes back via notification
 
    def sendNotification(self, notification):
        print(f"[Researcher] Received notification from NotificationService: {notification}")
 