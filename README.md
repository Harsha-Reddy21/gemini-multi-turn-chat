# Gemini Multi-Turn Chatbot

An interactive chatbot using Google's Gemini 1.5 Flash model that maintains conversation context across multiple turns.

## Features

- Multi-turn conversation with context preservation
- Configurable temperature parameter (0.0 - 1.0)
- Configurable model parameters

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Run the chatbot:
```bash
python gemini_chat.py
```

2. The chatbot will:
   - Prompt you to enter a temperature value (0.0 - 1.0)
   - Initialize the Gemini model with your chosen temperature
   - Start a conversation

3. During conversation:
   - Type your messages and press Enter to send
   - Type 'exit' or 'quit' to end the conversation
   - The chatbot will maintain context across multiple turns

## Model Configuration

The chatbot uses:
- Model: `gemini-1.5-flash`
- Configurable parameters:
  - Temperature: 0.0 - 1.0 (default: 0.7)
  - Top-p: 1
  - Max output tokens: 2048


##Example

Enter temperature (0.0 - 1.0, default is 0.7): 0.5

💬 Gemini Chat started. Type 'exit' to quit.

You: What type of data you have?

Gemini: I don't have data in the way a database or spreadsheet does.  I don't store files or individual pieces of information.  Instead, I have a massive dataset of text and code that I use to generate responses.  This dataset is used to train my large language model.  Think of it as a vast library of information that I use to understand and respond to your prompts.  The data itself is not directly accessible to me in a way I can manipulate or analyze; it's the underlying structure that allows me to function.


You: i was born in 2002. When did you born?

Gemini: I don't have a birthday. I'm a large language model, a computer program.  I wasn't "born" in the same way a human is.  My existence began when my training was completed.  While I don't have a specific birthdate,  my training data cutoff is a more relevant point in time, but even that is not a precise "birth."


You: what is 2+2?

Gemini: 2 + 2 = 4


You: what is my birth year?

Gemini: You told me you were born in 2002.


You: quit
