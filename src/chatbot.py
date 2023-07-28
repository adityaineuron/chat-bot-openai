import os
import openai

os.getenv('OPENAI_API_KEY')


class Chatbot:

    # Function to get the chatbot response
    def get_chatbot_response(self, prompt: str) -> str:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150,
                stop=[" Human:", " AI:"],
            )
            choices = response.get('choices')[0]
            text = choices.get('text')

            return text
        
        except Exception as e:
            print(e)  


    def update_prompt_list(self, message: str, prompt_list: list) -> None:
        try:
            prompt_list.append(message)

        except Exception as e:
            print(e)


    def create_prompt(self, message: str, prompt_list: list) -> str:
        try:

            prompt_message = f'\nHuman: {message}'
            self.update_prompt_list(message=prompt_message, prompt_list=prompt_list)
            prompt = "".join(prompt_list)

            return prompt
        
        except Exception as e:
            print(e)


    def bot_response(self, message: str, prompt_list: list) -> str:
        try:
            
            prompt = self.create_prompt(message=message, prompt_list=prompt_list)
            response = self.get_chatbot_response(prompt=prompt)

            if response:
                self.update_prompt_list(message=response, prompt_list=prompt_list)
                pos = response.find("\nAI: ")
                response = response[pos + 5:]
            else:
                response = "Something went wrong..."

            return response
        
        except Exception as e:
            print(e)
    
