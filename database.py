class Database:
    def __init__(self):
        self.submissions = []
        self.reviewers = [
            {"ID": 1, "name": "Reviewer 1", "workload": 2, "conflicts": []},
            {"ID": 2, "name": "Reviewer 2", "workload": 5, "conflicts": []},
            {"ID": 3, "name": "Reviewer 3", "workload": 1, "conflicts": [15]},
        ]
 
    # Step 5: Database.saveSubmission(data)
    def saveSubmission(self, data):
        print("[Database] - saveSubmission(self, data) - Received request to save submission")
        self.submissions.append(data)
        return "confirmation"
 
    # Step 7: Database.fetchReviewers()
    def fetchReviewers(self):
        print("[Database] - fetchReviewers(self) - Received request to fetch reviewers")
        return self.reviewers
    
    def saveScore(self, score):
        print(f"[Database] - saveScore(self, score) - Received request to save score: {score}")
    