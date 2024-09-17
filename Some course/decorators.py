# decorators

""""""

import requests
from requests.exceptions import RequestException
import time

# def my_decorators(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# # def say_hello():
# #     print("Hello")
# #
# #
# # my_decorators(say_hello)()
#
# @my_decorators
# def say_hello():
#     print("Hello")
#
#
# say_hello()


# def my_decorators(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         result = func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#         return result
#
#     return wrapper
#
#
# # @my_decorators
# # def say_hello(*, name: str) -> None:
# #     print(f"Hello, {name}")
# #
# #
# # say_hello(name="Sasha")
#
# @my_decorators
# def add_numbers(*, a: int, b: int) -> int:
#     print("Adding numbers...")
#     return a + b
#
#
# result = add_numbers(a=3, b=4)
#
# print(result)

API_KEY = "BQGPUW9HYTACK9GUGMCWBNFE5"


def retry(func):
    def wrapper_retry(*args, **kwargs):
        retries = [5, 30]
        for seconds in retries:
            try:
                return func(*args, **kwargs)
            except RequestException:
                print(f"Failed to get data. Retrying in {seconds} seconds")
                time.sleep(seconds)
        return func(*args, **kwargs)

    return wrapper_retry


@retry
def get_weather_by_hours_for_day_from_api(*, date: str, city: str) -> list[dict]:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?unitGroup=us&key={API_KEY}"
    response = requests.get(url)
    weather_by_days = response.json()["days"]
    weather_by_hours = weather_by_days[0]["hours"]
    return weather_by_hours


def fahrenheit_to_celsius(*, fahrenheit_temperature: float) -> int:
    return round((fahrenheit_temperature - 32) * 5 / 9)


def get_dangerous_hours(*, weather_by_hour: list[dict]) -> list[dict]:
    dangerous_hours = []
    for weather in weather_by_hour:
        uvindex = weather["uvindex"]
        time = weather["datetime"]
        celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature=weather["temp"])
        if uvindex >= 3:
            dangerous_hours.append({"time": time, "uvindex": uvindex, "temperature": celsius_temperature})

    return dangerous_hours


date = "2023-08-04"
city = "London,UK"
weather_by_hour = get_weather_by_hours_for_day_from_api(date=date, city=city)
dangerous_hours = get_dangerous_hours(weather_by_hour=weather_by_hour)
print(dangerous_hours)
