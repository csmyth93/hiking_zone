from pydantic import BaseModel
from typing import Literal


class Location(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    type: Literal["forest", "coastal"]
    description: str
    drive_time: str
    walk_url: str


class LocationsResponse(BaseModel):
    locations: list[Location]


class HourlyPrecipitation(BaseModel):
    hour: int  # 0-23
    precipitation_mm: float


class GridPoint(BaseModel):
    latitude: float
    longitude: float
    precipitation_mm: float  # Total for 9am-5pm


class LocationWeather(BaseModel):
    location_id: int
    hourly: list[HourlyPrecipitation]  # Hours 9-17 (9am-5pm)
    total_mm: float  # Total precipitation 9am-5pm


class WeatherResponse(BaseModel):
    date: str
    grid: list[GridPoint]
    locations: list[LocationWeather]
