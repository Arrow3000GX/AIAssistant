import requests

api_key = "31d03ef652251c5514b702756f922b75ddecd57e0fe4e0808ebb01915af4c1d2"
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
