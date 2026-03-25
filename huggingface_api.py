import os
import requests

def main():
    try:
        api_key = os.getenv("HF_API_KEY")

        if not api_key:
            raise ValueError("API key not found")

        user_input = input("Enter your prompt: ")

        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.post(
            "https://router.huggingface.co/hf-inference/models/gpt2",
            headers=headers,
            json={"inputs": user_input}
        )

        data = response.json()

        if isinstance(data, list):
            print("\nResponse:\n", data[0]["generated_text"])
        else:
            print("Error:", data)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()