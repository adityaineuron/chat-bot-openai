import os
import openai

os.getenv('OPENAI_API_KEY')

class Chatbot:

    # Function to get the chatbot response
    def get_chatbot_response(self, user_query):
        prompt = "user: " + user_query + "\n" + "chatbot:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            n=1,
            stop=["\n"],
        )
        return response.choices[0].text.strip()    