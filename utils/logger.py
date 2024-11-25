from datetime import datetime, timezone
from utils.config import ACCOUNT_AGE_THRESHOLD, KEYWORD_LIST

def create_log_message(message, flag_count):
    account_age = datetime.now(tz=timezone.utc) - message.author.created_at
    account_age_flag = "Yes" if account_age < ACCOUNT_AGE_THRESHOLD else "No"
    link_flag = "Yes" if "http" in message.content.lower() else "No"
    keyword_count = sum(1 for keyword in KEYWORD_LIST if keyword in message.content.lower())
    mention_flag = "Yes" if message.mention_everyone else "No"

    return f"""
    💀 **Message Deleted** <t:{int(datetime.now().timestamp())}:R>
    Username: {message.author} ({message.author.id})
    Was account age < 14 days? {account_age_flag}
    Link detected? {link_flag}
    Keywords flagged: {keyword_count}
    @everyone/@here mentioned? {mention_flag}
    Total flags: {flag_count}
    """
