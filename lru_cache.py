# home-made rough lru cache

import functools
import operator 
import sys
import threading
import time

lock = threading.Lock()

def cache_hash(*args, **kwargs):

	keys = args

	for item in kwargs.items():
		keys += item
	
	hashes = map(hash, keys)
	return functools.reduce(operator.xor, hashes)

def lru_cache(maxsize=128):

	if maxsize is not None and not isinstance(maxsize, int):
		raise TypeError('maxsize should be an integer or None')

	cache = {}

	def wrapper(func):

		def deco(*args, **kwargs):

			nonlocal cache
			key = cache_hash(*args, **kwargs)

			if cache.get(key):
				result = cache.get(key)
				cache.pop(key)
				cache[key] = result
				return result
			else:
				result = func(*args, **kwargs)
				if len(cache) == maxsize:
					cache.pop(list(cache.keys())[0])
					cache[key] = result
				else:
					cache[key] = result
				return result

		return deco

	return wrapper

@lru_cache(maxsize=64)
def fibs(*args, **kwargs):

	if args[0] < 2:
		return args[0]

	return fibs(args[0]-1) + fibs(args[0]-2)


def test():

	start = time.time()

	print(list(fibs(i) for i in range(30)))

	print('total time {}'.format(time.time() - start))	

if __name__ == '__main__':

	test()


