#!/usr/bin/env python3
""" Main file """
import redis

get_page = __import__('web').get_page

store = redis.Redis()

URL = "http://slowwly.robertomurray.co.uk"
count_key = "count:" + URL
print(store.get(count_key))

get_page(URL)
get_page(URL)
get_page(URL)
get_page(URL)
get_page(URL)
print(store.get(count_key))
