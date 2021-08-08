from app.models.location import Location
from app.models.weather_status import WeatherStatus
import httpx


async def request_weather_stat(location: Location) -> dict:
    """ Get weather status from https://weather.talkpython.fm/api/weather """

    url = f"https://weather.talkpython.fm/api/weather?" \
          f"city={location.city}" \
          f"&country={location.country}"
    if location.state:
        url += f"&state={location.state}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    return parse_resp_to_weather_stat(resp.json())


def parse_resp_to_weather_stat(data: dict) -> WeatherStatus:
    """ Parse the json response from https://weather.talkpython.fm/api/weather 
        into a WeatherStatus object and return it.
    """

    location = data.get('location', {})
    weather = data.get('weather', {})
    forecast = data.get('forecast', {})

    return WeatherStatus(
        location=Location(
            city=location.get("city", "N/A"),
            state=location.get("state", "N/A"),
            country=location.get("country", "N/A"),
        ),
        weather=weather.get("category", "N/A"),
        description=weather.get("description", "N/A"),
        temp=forecast.get("temp", 0.0),
        temp_feeling=forecast.get("feels_like", 0.0),
        temp_low=forecast.get("low", 0.0),
        temp_high=forecast.get("high", 0.0),
        humidity=forecast.get("humidity", 0.0),
    )
