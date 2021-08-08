from pydantic import BaseModel
from app.models.location import Location


class WeatherStatus(BaseModel):
    """ Model defines the weather status of a location. """

    location: Location
    weather: str = "N/A"
    description: str = "N/A"
    temp: float = 0.0
    temp_feeling: float = 0.0
    temp_low: str = "N/A"
    temp_high: str = "N/A"
    humidity: str = "N/A"
