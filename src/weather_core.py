from typing import Dict, Any, Optional, List
from dataclasses import dataclass



@dataclass
class WeatherData:
    """DTO (Data Transfer Object) для хранения погодных данных"""
    city: str
    country: str
    region: str
    local_time: str
    temperature: float
    feels_like: float
    condition: str
    humidity: int
    wind_speed: float
    wind_direction: str
    pressure: float
    visibility: float
    precipitation: float
    uv_index: Optional[float] = None
    icon: Optional[str] = None


@dataclass
class HourlyForecast:
    """DTO для почасового прогноза"""
    time: str
    temperature: float
    feels_like: float
    condition: str
    humidity: int
    wind_speed: float
    chance_of_rain: int
    precipitation: float
    is_current_hour: bool = False


class WeatherAPI:
    """Класс для работы с WeatherAPI.com данный класс реализует Мария"""
    pass