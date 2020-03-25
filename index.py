import configparser
import requests
import sys


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(
        location, api_key)
    r = requests.get(url)
    return r.json()


def main():
    location = input('pass the city name : ')

    api_key = get_api_key()
    weather = get_weather(api_key, location)

    print('present temperature is  = ' + str(weather['main']['temp']))
    print('feels like temperature is  = ' + str(weather['main']['feels_like']))
    print('minimum temperature is  = ' + str(weather['main']['temp_min']))
    print('maximum temperature is  = ' + str(weather['main']['temp_max']))

    # print(weather)


if __name__ == '__main__':
    main()
