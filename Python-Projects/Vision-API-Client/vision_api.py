from openai import OpenAI
import base64

client = OpenAI(base_url="http://localhost:8880/v1", api_key="no-key")

def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

# 發送請求
response = client.chat.completions.create(
    model="local-model",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "這張監視器畫面中有出現可疑人物嗎？"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encode_image('p1.png')}"}}
            ]
        }
    ]
)
print(response.choices[0].message.content)