from src.chatbot import Chatbot


chatbot = Chatbot()


def main():
    try:
        prompt_list = [
            "Hi there! I'm your friendly chatbot. How can I assist you today?",
            "\nHuman: What is the capital of India?"
            "\nAI: New Delhi"
        ]

        while True:
            user_input = input("You: ")
            response = chatbot.bot_response(message=user_input, prompt_list=prompt_list)
            print(f"Bot: {response}")

    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()