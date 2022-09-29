from environ.environ import Env

DEFAULTS = {
    "ENV": (str, "dev"),
    "DEBUG": (bool, True),
    "SECRET_KEY": (str, "secret-key"),
    "OPENWEATHERMAP_API_KEY": (str, "openweathermap-api-key"),
}

env = Env(**DEFAULTS)
