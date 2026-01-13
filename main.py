from src.weather_backend import WeatherApp


def main():
    """Точка входа в приложение"""
    app = WeatherApp()
    app.run()


if __name__ == "__main__":
    main()
