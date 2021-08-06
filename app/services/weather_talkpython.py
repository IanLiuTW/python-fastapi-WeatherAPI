from app.models.location import Location
import httpx


async def request_weather_stat(location: Location) -> dict:
    url = f"https://weather.talkpython.fm/api/weather?" \
          f"city={location.city}" \
          f"&country={location.country}"
    if location.state:
        url += f"&state={location.state}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    return resp.json()
