# Shared data objects used across all 

class Submission:
    def __init__(self, title, content, researcher_id):
        self.title = title
        self.content = content
        self.researcher_id = researcher_id

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "researcher_id": self.researcher_id,
        }

class ReviewData:
    def __init__(self, id, name, workload, conflicts):
        self.id = id
        self.name = name
        self.workload = workload
        self.conflicts = conflicts

class EvaluationResult:
    def __init__(self, outcome, average_score, consensus):
        self.outcome = outcome
        self.average_score = average_score
        self.consensus = consensus
        