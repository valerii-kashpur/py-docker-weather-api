import requests
import os

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
CITY = os.getenv("CITY")


def get_weather() -> None:
    res = requests.get(BASE_URL + f"?q={CITY}&key={API_KEY}")
    print("Performing request to Weather API for city Paris...")
    data = res.json()
    print(
        f"{data['location']['name']}/{data['location']['country']}"
        f" {data['location']['localtime']}"
        f" Weather: {data['current']['temp_c']} Celsius,"
        f" {data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
