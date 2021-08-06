from pydantic import BaseModel
from typing import Optional


class WeatherStat(BaseModel):
    city: str = "N/A"
    state: Optional[str] = "N/A"
    country: str = "N/A"
    weather: str = "N/A"
    description: str = "N/A"
    temp: float = 0.0
    temp_feeling: float = 0.0
    temp_low: str = "N/A"
    temp_high: str = "N/A"
    humidity: str = "N/A"
