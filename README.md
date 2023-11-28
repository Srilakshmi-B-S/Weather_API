
# Backend API for Weather Forecast

## Weather API with Flask
This project implements a simple Flask API that retrieves weather information from the OpenWeatherMap API based on user input. This Flask application serves as an API for retrieving weather information for a specified city. It integrates with the OpenWeatherMap API to provide details such as temperature, description, humidity, wind speed, and more.

## Prerequisites
1.Python3

2.Flask

3.OpenWeatherMap API Key 


## Brief Procedure
1.	Install all the required libraries.
2.	Get your OpenWeatherMap API Key by signing in with the OpenWeatherMap website.
3.	Run the code in any platform, Example: Visual Studio.
4.	Open Postman and create a new request to http://127.0.0.1:5000/weather with the GET method.
5.	Add a query param location with the value being the city and state (eg: Mysuru, KA).
6.	Send the request and check the output.
7.	NOTE: You can check the accuracy of the retrieved weather data by using OpenWeatherMap.

## Detailed Procedure
1.	Run the python script in VScode
2.	In the terminal you can see the base url http://127.0.0.1:5000. When you click on this url, you will see 404 error.
3.	Now go to your Postman workspace, set the request type to GET.
4.	Enter the URL for your Flask API endpoint i.e, http://127.0.0.1:5000/weather?.
5.	Click on the "Params" tab. In the "Key" column, enter location. In the "Value" column, enter the city and state for which you want to retrieve the weather information.
6.	Click the send button to make the request.
7.	Now go back to the base url, inorder to fetch the weather data, you have to append the base url with the api endpoint i.e, http://127.0.0.1:5000/weather?location=city,state
8.	(eg: http://127.0.0.1:5000/weather?location=Bengaluru, Karnataka&location=Mysore, Karnataka).
9.	Now you can see the json file.



## Usage
Ensure the server is running.
To retrieve weather information, make a GET request to the /api/weather endpoint with the city parameter.


## API Endpoint
/api/weather: Get weather information for a specific city.

Parameters:
   city (required): The name of the city for which you want weather information.
   
Example: curl http://localhost:5000/api/weather?city=NewYork


## Configuration
To use this project, you need to obtain an API key from OpenWeatherMap and update the configuration.
1.	Search for OPENWEATHERMAP_API_KEY in the code.
2.	Replace the Key with your actual OpenWeatherMap API key.


## Contributing
Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

## Screenshots
![image](https://github.com/Srilakshmi-B-S/Weather_API/assets/141704657/b84462b4-ab85-444f-b442-3b6d0f99817f)

![image](https://github.com/Srilakshmi-B-S/Weather_API/assets/141704657/576c2030-b27d-40c9-917a-cc53b2d4bbfe)

![image](https://github.com/Srilakshmi-B-S/Weather_API/assets/141704657/0a56e592-8c30-48d3-8117-6dc982e51316)

![image](https://github.com/Srilakshmi-B-S/Weather_API/assets/141704657/9a36cace-fb3f-40b4-bad5-8fcf09308466)







