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
            "max_tokens": 100,
            "temperature": 0.7,
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(f"{AI_BASE_URL}/completions", headers=headers, json=data) as response:
                    # Check for HTTP errors
                    if response.status == 200:
                        response_data = await response.json()
                        
                        # Validate if "choices" exists in the response
                        if "choices" in response_data and response_data["choices"]:
                            result = response_data["choices"][0].get("text", "").strip()
                            return result.lower() == "scam"
                        else:
                            print(f"Invalid response format: {response_data}")
                            return False
                    else:
                        # Log HTTP error details
                        error_text = await response.text()
                        print(f"HTTP Error {response.status}: {error_text}")
                        return False
            except aiohttp.ClientError as e:
                # Log network errors
                print(f"Network error: {e}")
                return False
            except Exception as e:
                # Catch unexpected errors
                print(f"Unexpected error: {e}")
                return False
