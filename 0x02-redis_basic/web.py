#!/usr/bin/env python3
''' Implement expiring web cache and tracker '''
import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def count(method: Callable) -> Callable:
    ''' Count method '''
    @wraps(method)
    def wrapper(*args, **kwargs):
        ''' wrapper '''
        r.incr('count:' + args[0])
        p = r.get(args[0])
        if not p:
            p = method(*args, **kwargs)
            r.setex(args[0], 10, p)
        return p
    return wrapper


@count
def get_page(url: str) -> str:
    ''' Get page '''
    return requests.get(url).text
