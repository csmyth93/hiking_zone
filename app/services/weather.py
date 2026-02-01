import httpx
from datetime import date
from typing import Literal
from app.models.schemas import GridPoint, LocationWeather, HourlyPrecipitation
from app.services.locations import get_all_locations

Mode = Literal["callum", "robert"]

# Bounding boxes for each mode
BOUNDING_BOXES = {
    # Callum mode: SE England (covers all hiking locations from E7 0AR)
    "callum": {
        "min_lat": 50.7,
        "max_lat": 51.9,
        "min_lon": -0.8,
        "max_lon": 1.5,
    },
    # Robert mode: NW England (covers all hiking locations from WA12 9US)
    "robert": {
        "min_lat": 53.1,
        "max_lat": 54.4,
        "min_lon": -3.2,
        "max_lon": -1.5,
    },
}

# Grid size (8x8 = 64 points)
GRID_SIZE = 8

# Walking hours (9am to 5pm)
WALK_START_HOUR = 9
WALK_END_HOUR = 17  # 5pm (exclusive, so 9-17 gives us 9am-4pm inclusive)


def generate_grid_points(mode: Mode = "callum") -> list[tuple[float, float]]:
    """Generate an 8x8 grid of lat/lon points covering the region for the given mode."""
    bbox = BOUNDING_BOXES[mode]
    points = []
    lat_step = (bbox["max_lat"] - bbox["min_lat"]) / (GRID_SIZE - 1)
    lon_step = (bbox["max_lon"] - bbox["min_lon"]) / (GRID_SIZE - 1)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            lat = bbox["min_lat"] + (i * lat_step)
            lon = bbox["min_lon"] + (j * lon_step)
            points.append((round(lat, 4), round(lon, 4)))

    return points


async def fetch_hourly_precipitation(
    latitudes: list[float],
    longitudes: list[float],
    target_date: date
) -> list[list[float]]:
    """
    Fetch hourly precipitation from Open-Meteo API for multiple points.
    Returns list of 24-hour precipitation arrays for each point.
    """
    lat_str = ",".join(str(lat) for lat in latitudes)
    lon_str = ",".join(str(lon) for lon in longitudes)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat_str,
        "longitude": lon_str,
        "hourly": "precipitation",
        "start_date": target_date.isoformat(),
        "end_date": target_date.isoformat(),
        "timezone": "Europe/London"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, timeout=30.0)
        response.raise_for_status()
        data = response.json()

    # Handle single point vs multiple points response format
    if isinstance(data, list):
        return [
            point["hourly"]["precipitation"]
            for point in data
        ]
    else:
        return [data["hourly"]["precipitation"]]


def sum_walking_hours(hourly_precip: list[float]) -> float:
    """Sum precipitation during walking hours (9am-5pm)."""
    return sum(hourly_precip[WALK_START_HOUR:WALK_END_HOUR + 1] or [0])


def extract_walking_hours(hourly_precip: list[float]) -> list[HourlyPrecipitation]:
    """Extract precipitation for each walking hour (9am-5pm)."""
    return [
        HourlyPrecipitation(
            hour=hour,
            precipitation_mm=hourly_precip[hour] if hourly_precip[hour] else 0.0
        )
        for hour in range(WALK_START_HOUR, WALK_END_HOUR + 1)
    ]


async def get_weather_data(target_date: date, mode: Mode = "callum") -> tuple[list[GridPoint], list[LocationWeather]]:
    """
    Get hourly precipitation data for the grid and all hiking locations.
    """
    # Generate grid points for the selected mode
    grid_coords = generate_grid_points(mode)
    grid_lats = [p[0] for p in grid_coords]
    grid_lons = [p[1] for p in grid_coords]

    # Get location coordinates for the selected mode
    locations = get_all_locations(mode)
    loc_lats = [loc.latitude for loc in locations]
    loc_lons = [loc.longitude for loc in locations]

    # Combine all coordinates for a single API call
    all_lats = grid_lats + loc_lats
    all_lons = grid_lons + loc_lons

    # Fetch hourly precipitation for all points
    all_hourly = await fetch_hourly_precipitation(all_lats, all_lons, target_date)

    # Split results
    grid_hourly = all_hourly[:len(grid_coords)]
    loc_hourly = all_hourly[len(grid_coords):]

    # Build grid points response (total precipitation during walking hours)
    grid_points = [
        GridPoint(
            latitude=grid_coords[i][0],
            longitude=grid_coords[i][1],
            precipitation_mm=sum_walking_hours(grid_hourly[i])
        )
        for i in range(len(grid_coords))
    ]

    # Build location weather response with hourly breakdown
    location_weather = [
        LocationWeather(
            location_id=locations[i].id,
            hourly=extract_walking_hours(loc_hourly[i]),
            total_mm=sum_walking_hours(loc_hourly[i])
        )
        for i in range(len(locations))
    ]

    return grid_points, location_weather
