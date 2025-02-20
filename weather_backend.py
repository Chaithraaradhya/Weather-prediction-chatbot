from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
API_KEY = "e477683090113d422469d964bc05405b"

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        return {
            "weather": f"The weather in {city_name} is '{weather}'. The temperature is {temperature}°C, feels like {feels_like}°C."
        }
    elif response.status_code == 404:
        return {"error": "City not found. Please check the city name."}
    else:
        return {"error": "Unable to fetch weather data. Please try again later."}

@app.route('/weather', methods=['GET'])
def weather_endpoint():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City name is required."}), 400
    
    weather_data = get_weather(city)
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug=True)
