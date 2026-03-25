import os
from google import genai

def main():
    try:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("API key not found")

        client = genai.Client(api_key=api_key)

        user_input = input("Enter your prompt: ")

        response = client.models.generate_content(
           model="gemini-1.5-flash",
            contents=user_input
        )

        print("\nResponse:\n", response.text)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()