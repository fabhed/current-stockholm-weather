from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_weather_data():
    """Fetches the current weather data for Stockholm from OpenWeatherMap API."""
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Stockholm&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    """Renders the main page with the current weather in Stockholm."""
    weather_data = get_weather_data()
    temperature = weather_data['main']['temp']
    return render_template('index.html', temperature=temperature)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
