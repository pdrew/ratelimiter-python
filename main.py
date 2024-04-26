from fastapi import FastAPI, Request
from rate_limiter import RateLimiterFactory
from limiting_algorithms import RateLimitExceeded

app = FastAPI()
ip_addresses = {}


@app.get("/limited")
async def limited(request: Request):
    host = request.client.host
    try:
        if host not in ip_addresses:
            ip_addresses[host] = RateLimiterFactory.get_instance("SlidingWindow")
        if ip_addresses[host].allow_request():
            return { "status": "OK" }
    except RateLimitExceeded as e:
        raise e

@app.get("/unlimited")
async def unlimited(request: Request):
    return { "status": "OK" }