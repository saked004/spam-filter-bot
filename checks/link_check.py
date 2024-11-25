import re
from checks.base import Check

# 🟨2️⃣ Second check.
# # Check if the message contains a full link
class LinkCheck(Check):
    def is_flagged(self, message) -> bool:
        regex_link = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        return bool(re.search(regex_link, message.content) or re.search(r'discord.gg/', message.content))
