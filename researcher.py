from shared_objects import Submission

class Researcher:

    # Step 1: Researcher -> UI : submitResearchOutput(data)
    def submitResearchOutput(self):
        print("[Researcher] Submitting research output...")

        submission = Submission(
            title="Differential Evolution for image registration"
            content="A software system grounded on Differential Evolution to automatically..."
            reseracher_id=15
        ) 