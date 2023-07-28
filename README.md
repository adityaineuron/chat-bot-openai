# chat-bot-openai

This chatbot project utilizes the OpenAI API to create an interactive and versatile AI-powered conversational agent. The chatbot leverages the text-davinci-003 model to understand and respond to natural language inputs from users. With a focus on context and coherence, the chatbot can engage in meaningful and informative conversations. It can answer questions, provide recommendations, share jokes and fun facts, and even perform basic calculations. The project aims to enhance user experience by delivering human-like interactions and catering to various user needs. The chatbot's potential applications include customer support, information retrieval, language translation, and more, making it a valuable tool for engaging with users and facilitating communication in a wide range of scenarios. Throughout the development process, ethical and responsible AI practices were followed to ensure a safe and beneficial user experience.


## Adding openapi key to environment variables

Step 1. Search for 'Edit the system environment variables' in control panel.

Step 2. Click on 'Environment variables' 

Step 3. Click on new button for adding environment variable for openapi key

Step 4. Give variable name as 'OPENAI_API_KEY' and varaible value should be your openapi key

Step 5. click on ok


## How to run?

Step 1. Cloning the repository.

```bash
git clone https://github.com/adityaineuron/chat-bot-openai
```

Step 2. Create a conda environment.

```bash
conda create -p env python=3.8 -y
```

Step 3. Activate the environment - 

```bash
conda activate env/
```

Step 4. Install necessary requirements

```bash
pip install -r requirements.txt
```

Step 5. Run the main.py file

```bash
python main.py
```