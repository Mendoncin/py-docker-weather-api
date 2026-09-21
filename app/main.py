import os
import requests

API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> dict:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    params = {
        "key": api_key,
        "q": "Paris",
    }

    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def main() -> None:
    weather = get_weather()

    location = weather["location"]
    current = weather["current"]

    print(
        "{}/{} {} Weather: {} Celsius, {}".format(
            location["name"],
            location["country"],
            location["localtime"],
            current["temp_c"],
            current["condition"]["text"],
        )
    )


if __name__ == "__main__":
    main()
