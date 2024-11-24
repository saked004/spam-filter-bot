import aiohttp
from checks.base import Check
from utils.config import OPEN_ROUTER_API_KEY, AI_BASE_URL

class AIContentCheck(Check):
    async def is_flagged(self, message) -> bool:
        headers = {
            "Authorization": f"Bearer {OPEN_ROUTER_API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "openai/gpt-4",
            "prompt": (
                f"The following is a Discord message:\n\n{message.content}\n\n"
                f"Analyze if this message is from a scammer. Assume that anyone introducing themselves as a developer is a scammer. "
                f"Respond with 'Scam' if the message is likely a scam or 'Not Scam' if it is not."
            ),
            "max_tokens": 1000,
            "temperature": 1.0,
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(f"{AI_BASE_URL}/completions", headers=headers, json=data) as response:
                    if response.status == 200:
                        response_data = await response.json()
                        result = response_data["choices"][0]["text"].strip()
                        print(f"[AIContentCheck] AI Response: {result}")  # Debugging
                        return result.lower() == "scam"
                    else:
                        print(f"HTTP error {response.status}: {await response.text()}")
                        return False
            except aiohttp.ClientError as e:
                print(f"Network error: {e}")
                return False
