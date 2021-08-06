import fastapi
from app.models.location import Location
from app.models.weather_stat import WeatherStat
from app.services.weather_talkpython import request_weather_stat

router = fastapi.APIRouter()


@router.get('/', response_model=WeatherStat)
async def weather_stat(location: Location = fastapi.Depends()) -> WeatherStat:
    resp = await request_weather_stat(location)
    weather_stat = parse_resp_to_weather_stat(resp)
    return weather_stat


def parse_resp_to_weather_stat(data: dict) -> WeatherStat:
    location = data.get('location', {})
    weather = data.get('weather', {})
    forecast = data.get('forecast', {})

    return WeatherStat(
        city=location.get("city", "N/A"),
        state=location.get("state", "N/A"),
        country=location.get("country", "N/A"),
        weather=weather.get("category", "N/A"),
        description=weather.get("description", "N/A"),
        temp=forecast.get("temp", 0.0),
        temp_feeling=forecast.get("feels_like", 0.0),
        temp_low=forecast.get("low", 0.0),
        temp_high=forecast.get("high", 0.0),
        humidity=forecast.get("humidity", 0.0),
    )
