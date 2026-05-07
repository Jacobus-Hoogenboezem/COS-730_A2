class NotificationService:
    def __init__(self, researcher):
        self.researcher = researcher

    # Step 18 (alt accepted): NotificationService.notifyAcceptance()
    def notifyAcceptance(self):
        print("[NotificationService] Acceptance notification sent.")
        self.researcher.sendNotification("Accepted")

    # Step 18 (alt rejected): NotificationService.notifyRejection()
    def notifyRejection(self):
        print("[NotificationService] Rejection notification sent.")
        self.researcher.sendNotification("Rejected")

    # Step 18 (alt revision): NotificationService.notifyRevision()
    def notifyRevision(self):
        print("[NotificationService] Revision notification sent.")
        self.researcher.sendNotification("Revision")