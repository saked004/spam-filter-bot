
# 📗 Standard library imports (no need to install)
import os
from datetime import timedelta

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇
# ⚙️ Settings/configurable variables
# # The threshold for the account age check
# Minimum account age in days
ACCOUNT_AGE_THRESHOLD = timedelta(days=5)
# # Not case-sensitive, do not use plural forms.
KEYWORD_LIST = ['onlyfan', 'teen', 'leak', 'nude']
# # The ID of the admin log channel where the bot will send the log messages
# Replace with the IDs of the whitelisted channels
ADMIN_LOG_CHANNEL_ID =os.getenv("ADMIN_LOG_CHANNEL_ID")
# # The bot token for the Discord bot 
# # Found in the Discord Developer Portal at https://discord.com/developers/applications
# # Replace with your bot token!
DISCORD_BOT_TOKEN =os.getenv("DISCORD_BOT_TOKEN")

OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY") 

AI_BASE_URL = os.getenv("AI_BASE_URL")

# ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️

# Validate environment variables
if not DISCORD_BOT_TOKEN or not OPEN_ROUTER_API_KEY:
    raise EnvironmentError("Missing required environment variables: DISCORD_BOT_TOKEN or OPEN_ROUTER_API_KEY")

# Spam detection settings

