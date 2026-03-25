import os
from groq import Groq

def main():
    try:
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("API key not found. Set GROQ_API_KEY.")

        client = Groq(api_key=api_key)

        user_input = input("Enter your prompt: ")

        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input}
            ],
            model="llama-3.1-8b-instant"   # ✅ CURRENT WORKING MODEL
        )

        print("\nResponse:\n", response.choices[0].message.content)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()