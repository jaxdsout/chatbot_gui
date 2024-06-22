from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Chatbot:
    def get_response(self, user_input):
        res = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5).choices[0].text.strip()
        return res


if __name__ == "__main__":
    chatter = Chatbot()
    response = chatter.get_response("Write a joke about birds")
    print(response)