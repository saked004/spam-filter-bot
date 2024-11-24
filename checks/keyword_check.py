from checks.base import Check
from utils.config import KEYWORD_LIST

# 🟨3️⃣ Third check.
# # Check if the message contains any of the keywords
class KeywordCheck(Check):
    def is_flagged(self, message) -> bool:
        formatted_message = message.content.lower().replace(' ', '')
        return any(keyword in formatted_message for keyword in KEYWORD_LIST)
