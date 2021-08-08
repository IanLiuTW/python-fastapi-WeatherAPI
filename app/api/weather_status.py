import fastapi
from app.models.location import Location
from app.models.weather_status import WeatherStatus
from app.services.weather_talkpython import request_weather_stat


router = fastapi.APIRouter()


@router.get('/', response_model=WeatherStatus)
async def weather_stat(location: Location = fastapi.Depends()) -> WeatherStatus:
    weather_stat = await request_weather_stat(location)
    return weather_stat
