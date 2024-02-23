import requests
from dotenv import load_dotenv

class ModelBack:
    def __init__(self):
        load_dotenv()  # 加载环境变量
        self.url = os.getenv("OPENAI_API_URL")
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + os.getenv("OPENAI_API_KEY")
        }

    def generate(self, role_config, question):
        try:
            data = {
                "model": "gpt-3.5-turbo-16k",
                "messages": [
                    {"role": "system", "content": role_config},
                    {"role": "user", "content": question}
                ],
                "temperature": 0
            }

            response = requests.post(self.url, headers=self.headers, json=data)
            answer = response.json()["choices"][0]["message"]["content"].strip()
            return answer
        except Exception as exc:
            print(exc)
            return None