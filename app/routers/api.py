from fastapi import APIRouter, Query
from datetime import date
from typing import Literal

from app.models.schemas import LocationsResponse, WeatherResponse
from app.services.locations import get_all_locations
from app.services.weather import get_weather_data

router = APIRouter(prefix="/api", tags=["api"])

Mode = Literal["callum", "robert"]


@router.get("/locations", response_model=LocationsResponse)
async def get_locations(
    mode: Mode = Query(default="callum", description="User mode: callum (London) or robert (Newton-le-Willows)")
):
    """Return all 20 hiking locations with coordinates and details for the selected mode."""
    locations = get_all_locations(mode)
    return LocationsResponse(locations=locations)


@router.get("/weather", response_model=WeatherResponse)
async def get_weather(
    date_param: date = Query(default=None, alias="date", description="Date for weather forecast (YYYY-MM-DD)"),
    mode: Mode = Query(default="callum", description="User mode: callum (London) or robert (Newton-le-Willows)")
):
    """
    Return precipitation data for the specified date and mode.
    Includes an 8x8 grid for the rain overlay and each location's forecast.
    """
    if date_param is None:
        date_param = date.today()

    grid_points, location_weather = await get_weather_data(date_param, mode)

    return WeatherResponse(
        date=date_param.isoformat(),
        grid=grid_points,
        locations=location_weather
    )
