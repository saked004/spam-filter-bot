from checks.base import Check

# 🟨4️⃣ Fourth check
# # Check if the message mentions @everyone
class MentionCheck(Check):
    def is_flagged(self, message) -> bool:
        return message.mention_everyone
