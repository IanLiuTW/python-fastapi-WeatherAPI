from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    """ Model defines a location """

    city: str = "Taipei"
    state: Optional[str] = None
    country: str = "TW"
