class Validator:
    # SD-Step 3: Validator receives validateFormat(data) from SubmissionController
    def validateFormat(self, data):
        
        # Returns "valid" or "invalid"
        if not data.get("title") or not data.get("content"):
            return "invalid"

        return "valid"