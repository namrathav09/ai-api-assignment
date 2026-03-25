import requests

def main():
    try:
        user_input = input("Enter your prompt: ")

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:1b",
                "prompt": user_input,
                "stream": False
            }
        )

        data = response.json()

        # DEBUG: print full response (optional)
        # print(data)

        if "response" in data:
            print("\nResponse:\n", data["response"])
        else:
            print("Error from Ollama:", data)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()