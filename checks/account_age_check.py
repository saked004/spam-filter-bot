from datetime import datetime, timezone
from checks.base import Check
from utils.config import ACCOUNT_AGE_THRESHOLD

# 🟨1️⃣ First check.
# # Check if the message author's account is older than X day
class AccountAgeCheck(Check):
    def is_flagged(self, message) -> bool:
        account_age = datetime.now(tz=timezone.utc) - message.author.created_at
        return account_age < ACCOUNT_AGE_THRESHOLD
