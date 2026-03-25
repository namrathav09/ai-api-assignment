import os
import cohere

def main():
    try:
        api_key = os.getenv("COHERE_API_KEY")
        if not api_key:
            raise ValueError("API key not found")

        co = cohere.ClientV2(api_key)

        user_input = input("Enter your prompt: ")

        response = co.chat(
            model="command-r-08-2024",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        print("\nResponse:\n", response.message.content[0].text)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()