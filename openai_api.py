import os
from openai import OpenAI

def main():
    try:
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("API key not found")

        client = OpenAI(api_key=api_key)

        user_input = input("Enter your prompt: ")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_input}]
        )

        print("\nResponse:\n", response.choices[0].message.content)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()