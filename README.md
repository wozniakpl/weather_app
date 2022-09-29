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

If you want to try setting favourite coords, try this
```
# see that without login and favourite coords saved, lat/lon are required
curl -X GET \
    -H "Content-Type: application/json" \
    http://localhost:9000/weather/today/

# register
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "test", "password": "test", "first_name": "test", "last_name": "test"}' \
    http://localhost:9000/account/register/

# obtain token
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "test", "password": "test"}' \
    http://localhost:9000/api/token/

# set favourite coords
curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <token>" \
    -d '{"lat": 50.0, "lon": 50.0}' \
    http://localhost:9000/account/favourite-coords/

# get today's weather without providing coords
curl -X GET \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <token>" \
    http://localhost:9000/weather/today/

```