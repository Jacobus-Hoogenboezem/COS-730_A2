class Validator:
    # Step 3: Validator receives validateFormat(data) from SubmissionController
    def validateFormat(self, data):
        print("[Validator] Receiver validation request")
        # Step 4: Returns "valid" or "invalid"
        print("[Validator] Responding with validation result")
        if not data.get("title") or not data.get("content"):
            return "invalid"

        return "valid"