#!/usr/bin/env python3
"""something about redis"""
import redis
from functools import wraps
import requests
from typing import Callable

_redis = redis.Redis()


def get_page_count(method: Callable) -> Callable:
    """something about redis"""

    @wraps(method)
    def wrapper(*args):
        key = f"count:{args[0]}"
        _redis.incr(key)
        _redis.setex('count', 10, _redis.get(key))
        return method(*args)

    return wrapper


@get_page_count
def get_page(url: str) -> str:
    """something about redis"""
    req = requests.get(url)
    return req.text
