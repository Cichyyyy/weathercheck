import requests


def get_weather(city, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Retrieve relevant data
        city_name = data['location']['name']
        temperature = data['current']['temp_c']
        weather_description = data['current']['condition']['text']

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("Unable to retrieve weather data. Please check the city name and try again.")


def main():
    api_key = "YOUR_API_KEY"  # Your API Key
    city = input("Enter the city name: ")
    get_weather(city, api_key)


if __name__ == "__main__":
    main()
