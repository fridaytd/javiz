import os
import javiz
import httpx

url = f"https://discord.com/api/v10/applications/{os.getenv("APPLICATION_ID")}/commands"

payload = {
    "name": "hello",
    "type": 1,
    "description": "Say hello to bot",
}

headers = {
    "Authorization": f"Bot {os.getenv("APPLICATION_BOT_TOKEN")}",
}

r = httpx.post(
    url=url,
    headers=headers,
    json=payload,
)

print(r.status_code)
print(r.json())
