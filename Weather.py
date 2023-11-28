from flask import Flask, Blueprint, jsonify, request
import requests

# Create a Flask application
app = Flask(__name__)

# Configuration class for Flask app
class Config:
    DEBUG = False
    TESTING = False
    OPENWEATHERMAP_API_KEY = 'your_actual_api_key'  # Replace with your actual OpenWeatherMap API key

# Load configuration from Config class
app.config.from_object(Config)

# Create a Flask Blueprint for the API
api_bp = Blueprint('api_bp', __name__)

# Define a route for retrieving weather data
@api_bp.route('/weather', methods=['GET'])
def get_weather():
    # Get the 'city' parameter from the query string
    city = request.args.get('city')

    # Check if the 'city' parameter is missing
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400

    # Call the function to retrieve weather data
    weather_data = get_weather_data(city)

    # Check for errors in the weather data
    if 'error' in weather_data:
        return jsonify(weather_data), 500

    # Return the weather data as JSON
    return jsonify(weather_data)

# Function to retrieve weather data for a given city
def get_weather_data(city):
    # Get the OpenWeatherMap API key from the configuration
    api_key = Config.OPENWEATHERMAP_API_KEY

    # Construct the API URL for the weather data
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        # Make a request to the OpenWeatherMap API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse the JSON response

        # Extract relevant weather information from the API response
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'icon': get_weather_icon(data['weather'][0]['icon']),
            'min_temperature': data['main']['temp_min'],
            'max_temperature': data['main']['temp_max'],
            'pressure': data['main']['pressure'],
            'visibility': data.get('visibility', 'N/A'),
            'sunrise': convert_unix_timestamp(data['sys']['sunrise']),
            'sunset': convert_unix_timestamp(data['sys']['sunset']),
            'current_time': convert_unix_timestamp(data['dt']),
            'timezone': data['timezone']
        }

        # Return the weather information
        return weather

    except requests.exceptions.RequestException as e:
        # Handle exceptions (e.g., network errors)
        return {'error': f'Error fetching weather data: {e}'}

# Function to construct the URL for the weather icon
def get_weather_icon(icon_code):
    return f'http://openweathermap.org/img/w/{icon_code}.png'

# Function to convert a Unix timestamp to a human-readable format
def convert_unix_timestamp(timestamp):
    from datetime import datetime
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Register the API Blueprint with the app
app.register_blueprint(api_bp, url_prefix='/api')

# Run the Flask application if executed directly
if __name__ == '__main__':
    app.run(debug=True)
