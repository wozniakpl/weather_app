# Weather App

A simple, demonstrative app that covers:

- getting weather data (+ caching responses)
- register + login
- fav location for user

## How to

### Run

1. Provide `.env` (based on `.env.example`)

2. Run docker-compose

```sh
docker-compose up
```

### Test

```sh
docker-compose run --rm backend pytest
```

## Usage

Register: [http://localhost:9000/account/register/](http://localhost:9000/account/register/)

Get token: [http://localhost:9000/api/token/](http://localhost:9000/api/token/)

Get today's weather: [http://localhost:9000/weather/today/?lat=50.0&lon=50.0](http://localhost:9000/weather/today/?lat=50.0&lon=50.0)