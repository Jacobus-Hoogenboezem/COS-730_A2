class OutcomePolicy:

    def determineOutcome(self, avg, consensus):
        print("[OutcomePolicy] - determineOutcome(self, avg, consensus) - Applying outcome rules.")

        if not consensus:
            print("[OutcomePolicy] - WARNING: Reviewer consensus was NOT reached.")

        if avg >= 7:
            print(f"[OutcomePolicy] - Outcome: ACCEPTED (avg={avg:.2f})")
            return "accepted"
        elif avg >= 4:
            print(f"[OutcomePolicy] - Outcome: REVISION REQUIRED (avg={avg:.2f})")
            return "revision"
        else:
            print(f"[OutcomePolicy] - Outcome: REJECTED (avg={avg:.2f})")
            return "rejected"