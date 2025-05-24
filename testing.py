import requests

api_key = "31d0_YOUR_API_KEY_HERE"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "meta-llama/Llama-3-70b-chat-hf",
    "messages": [
        {"role": "user", "content": "Who wrote Harry Potter?"}
    ]
}

response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])
