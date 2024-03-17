import os

from openai import OpenAI
from dotenv import load_dotenv

class AiTool:
    
    def __init__(self):

        load_dotenv()

        self.client = OpenAI(api_key=os.environ.get("AI_API_KEY"))

    def GetSentiment(self, opinion: str) -> str:
        """
        Get sentiment from opinion summarized in one word.
        """

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You will recieve opinion about health resort. Answer in polish language. Your job is to get general sentiment toward the health resort and reply with only 1 word that summarizes it (your reply will be of 1 word length)."},
                {"role": "user", "content": opinion}
            ]
        )

        return completion.choices[0].message.content