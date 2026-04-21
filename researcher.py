from shared_objects import Submission

class Researcher:

    # Step 1: Researcher -> UI : submitResearchOutput()
    def submitResearchOutput(self):
        print("[Researcher] Submitting research output...")

        submission = Submission(
            title="Differential Evolution for image registration",
            content="A software system grounded on Differential Evolution to automatically...",
            researcher_id=15
        ) 

        print(f"[Researcher] Submission created: {submission.title}")
        return submission