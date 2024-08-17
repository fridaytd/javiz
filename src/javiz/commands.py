import os
import javiz
import httpx

url = f"https://discord.com/api/v10/applications/{os.getenv("APPLICATION_ID")}/commands"

hello_command = {
    "name": "hello",
    "type": 1,
    "description": "Say hello to bot",
}

lottery_command = {
    "name": "lottery",
    "type": 1,
    "description": "Get South of Vietnam lottery results",
}

headers = {
    "Authorization": f"Bot {os.getenv("APPLICATION_BOT_TOKEN")}",
}

r = httpx.post(
    url=url,
    headers=headers,
    json=lottery_command,
)

print(r.status_code)
print(r.json())
