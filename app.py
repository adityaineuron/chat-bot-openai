from flask import Flask, request, render_template
from src.chatbot import Chatbot


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/chat", methods=["POST"])
def chat():
    chatbot = Chatbot()
    user_query = request.form.get("query")
    bot_response = chatbot.get_chatbot_response(user_query)
 
    return render_template('home.html', query = user_query,
                           response=bot_response)


if __name__ == "__main__":
    app.run(debug=True)