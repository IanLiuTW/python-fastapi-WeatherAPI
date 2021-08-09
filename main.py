from fastapi import FastAPI
from app.api import weather_status


app = FastAPI()


@app.get("/", include_in_schema=False)
def root():
    return {
        "Examples": {
            "Taipei": "http://127.0.0.1:8000/api/weather_stat",
            "Seattle": "http://127.0.0.1:8000/api/weather_stat?country=US&city=Seattle&state=WA"
        }
    }


def configure(app):
    app.include_router(weather_status.router, prefix="/api/weather_stat")


configure(app)
