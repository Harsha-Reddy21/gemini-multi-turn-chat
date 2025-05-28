import google.generativeai as genai
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: Please set your GEMINI_API_KEY as an environment variable.")
        return

    genai.configure(api_key=api_key)

    try:
        temperature = float(input("Enter temperature (0.0 - 1.0, default is 0.7): ") or 0.7)
    except ValueError:
        temperature = 0.7
        print("Invalid input. Using default temperature = 0.7")

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={
            "temperature": temperature,
            "top_p": 1,
            "max_output_tokens": 2048,
        }
    )
    chat = model.start_chat(history=[])

    print("\n💬 Gemini Chat started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break

        try:
            response = chat.send_message(user_input)
            print(f"Gemini: {response.text}\n")
        except Exception as e:
            print("Error communicating with Gemini API:", e)
            break

if __name__ == "__main__":
    main()
