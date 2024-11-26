# 🌟 Spam Filter Bot v1.0

## Overview
The **Spam Filter Bot** is designed to counteract spam and scam messages in Discord servers. It intelligently evaluates messages based on multiple criteria, automatically removes spammy content, and notifies admins.  

## Features
1. **Account Age Check**  
   Flags accounts less than a configurable number of days old (default: 5 days).  
2. **Link Detection**  
   Identifies messages containing suspicious links or Discord invite links.  
3. **Keyword Detection**  
   Flags messages containing specific keywords (e.g., "fullstack", "blockchain", etc.).  
4. **Mentions Detection**  
   Detects messages containing excessive mentions of `@everyone` or `@here`.  
5. **AI-Based Scam Analysis**  
   Uses AI to analyze whether messages are likely scams, with specific emphasis on developers introducing themselves.  
6. **Timeout System**  
   Automatically applies a timeout to users who send flagged messages.  
7. **Admin Logging**  
   Logs flagged messages in a designated admin channel for review.  

---

## How It Works
The bot evaluates messages against **five checks**. If **two or more checks** are flagged, the message is considered spam:  
1. **Account Age**  
   Checks the age of the message sender's account.  
2. **Links**  
   Flags any messages with suspicious or invite links.  
3. **Keywords**  
   Scans for predefined suspicious keywords.  
4. **Mentions**  
   Identifies messages with excessive use of `@everyone` or `@here`.  
5. **AI Content Analysis**  
   Sends the message to an AI model for scam detection.  

When flagged, the bot will:
- **Delete the message**.
- **Log the incident** in the admin log channel.
- **Timeout the user** for a configurable period (default: 10 seconds).

---

## Setup Instructions

### Prerequisites
- Python 3.8+ installed.
- A Discord bot token.
- OpenRouter API key for AI analysis.
- Required permissions for the bot:  
  - `Manage Messages`  
  - `Timeout Members`  
  - `View Audit Log`

### Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/saked004/spam-filter-bot.git
   cd spam-filter-bot
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
    ```
3. Create a `.env` file in the project root and add your keys:
   ```env
   DISCORD_BOT_TOKEN=
   OPEN_ROUTER_API_KEY=
   ADMIN_LOG_CHANNEL_ID=
   AI_BASE_URL =
   TIME_OUT = 
   ```
4. Configure settings (optional):
Modify settings in the `utils/config.py` file, such as account age thresholds, keywords, and timeout duration.

## Running the Bot
- Start the bot with:
   ```bash
   python bot.py
   ```
## File Structure
   ```plaintext
   spam-filter-bot/
                    │
                    ├── bot.py               
                    ├── checks/               
                    │   ├── account_age_check.py
                    │   ├── link_check.py
                    │   ├── keyword_check.py
                    │   ├── mention_check.py
                    │   └── ai_check.py       
                    │
                    ├── utils/                
                    │   ├── config.py          
                    │   └── logger.py         
                    │
                    ├── requirements.txt      
                    ├── .env                  
                    └── README.md      
```
## Customization
**Modify Keywords**
- Edit KEYWORD_LIST in `checks/keyword_check.py` to add/remove keywords.

**Change Account Age Threshold**
- Update the `ACCOUNT_AGE_THRESHOLD` in `checks/account_age_check.py`.

**Adjust Timeout Duration**
- Modify the `TIMEOUT_DURATION` in `bot.py`(default: 10 seconds).

## License
This project is licensed under the MIT License.
