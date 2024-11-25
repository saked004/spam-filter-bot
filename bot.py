# 🌟 Spam Filter Bot v1.0
# This bot is designed to counter the recent wave of spam bots on Discord servers.
# 
# It checks for the following: [All are configurable]
# 1. Account age (less than 5 days)
# 2. Any links or invite links
# 3. Keywords from a list
# 4. @everyone or @here was mentioned
# 
# If any TWO OR MORE of the FOUR checks are flagged, the message is deleted automatically.
# An admin log is created for each deleted message.
#

import nextcord  # The Discord Bot API library
from datetime import timedelta  # Correctly import timedelta
from nextcord.ext import commands

from checks.account_age_check import AccountAgeCheck
from checks.link_check import LinkCheck
from checks.keyword_check import KeywordCheck
from checks.mention_check import MentionCheck
from checks.ai_check import AIContentCheck

from utils.config import DISCORD_BOT_TOKEN, ADMIN_LOG_CHANNEL_ID
from utils.logger import create_log_message

# Configure intents
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
client = nextcord.Client(intents=intents)


# SpamDetector Class
class SpamDetector:
    def __init__(self, checks):
        self.checks = checks

    async def get_flag_count(self, message) -> int:
        flag_count = 0
        for check in self.checks:
            if isinstance(check, AIContentCheck):
                is_flagged = await check.is_flagged(message)
            else:
                is_flagged = check.is_flagged(message)
            flag_count += is_flagged
            print(f"[SpamDetector] {check.__class__.__name__} Flagged: {is_flagged}")
        print(f"[SpamDetector] Total Flags: {flag_count}")
        return flag_count



# Instantiate SpamDetector
spam_detector = SpamDetector([
    AccountAgeCheck(),
    LinkCheck(),
    KeywordCheck(),
    MentionCheck(),
    AIContentCheck(),
])


@client.event
async def on_message(message):

    if message.author == client.user or message.type != nextcord.MessageType.default:
        return

    print(f"[on_message] Received Message: '{message.content}' by {message.author}")

    flag_count = await spam_detector.get_flag_count(message)
    print(f"[on_message] Flag Count: {flag_count}")

    if flag_count >= 2:
        await message.delete()  # Delete the message
        print(f"[on_message] Deleted Message: '{message.content}' by {message.author}")

        # Log to admin channel
        admin_log_channel = client.get_channel(ADMIN_LOG_CHANNEL_ID)
        if admin_log_channel:
            log_message = create_log_message(message, flag_count)
            await admin_log_channel.send(log_message)

        # Apply timeout to the user
        try:
            timeout_duration = timedelta(seconds=10)
            await message.author.timeout(timeout_duration)
            print(f"[on_message] User {message.author.name} timed out for 10 seconds.")
        except Exception as e:
            print(f"[on_message] Failed to timeout user {message.author.name}: {e}")

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")


# Run the bot
client.run(DISCORD_BOT_TOKEN)

