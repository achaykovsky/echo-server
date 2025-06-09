from flask import Request
from redis import Redis
from config import REDIS_HOST, REDIS_PORT

redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
REQUEST_COUNTER_KEY = "echo_server:request_count"


def increment_request_count() -> int:
    return redis_client.incr(REQUEST_COUNTER_KEY)


def parse_request_data(request: Request) -> dict:
    if request.method == "GET":
        return request.args.to_dict()
    if request.is_json:
        try:
            return request.get_json(force=True)
        except Exception:
            raise ValueError("Invalid JSON payload")
    return request.form.to_dict()
