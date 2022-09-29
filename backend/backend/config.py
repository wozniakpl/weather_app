from environ.environ import Env

DEFAULTS = {
    "ENV": (str, "dev"),
    "DEBUG": (bool, True),
    "SECRET_KEY": (str, "secret-key"),
    "OPENWEATHERMAP_API_KEY": (str, "openweathermap-api-key"),
    "POSTGRES_DB": (str, "weather"),
    "POSTGRES_USER": (str, "weather-user"),
    "POSTGRES_PASSWORD": (str, "weather-secret"),
    "POSTGRES_HOST": (str, "db"),
}

env = Env(**DEFAULTS)
