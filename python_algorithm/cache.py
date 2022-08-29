import collections


def cache_find(cacheSize:int, cities):
    elapsed: int = 0
    cache = collections.deque([], maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            elapsed += 1
        else:
            cache.append(c)
            elapsed += 5
    return elapsed
