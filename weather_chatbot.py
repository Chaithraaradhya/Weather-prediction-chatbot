import requests

def get_weather_from_backend(city_name):
    base_url = "http://127.0.0.1:5000/weather"
    params = {"city": city_name}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            return data["error"]
        return data["weather"]
    else:
        return "Unable to fetch weather data from the backend."

def chatbot():
    print("Hello! I am your Weather Chatbot 😊")
    print("Type 'exit', 'quit', or 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Stay safe 🌤️")
            break
        else:
            weather_info = get_weather_from_backend(user_input)
            print("Chatbot:", weather_info)

if __name__ == "__main__":
    chatbot()
