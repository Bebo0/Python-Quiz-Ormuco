import collections
import time
EXPIRES_AFTER = 600
class Cache(object):
	"""A Geo Distributed LRU (Least Recently Used) cache model"""
	def __init__(self, maxCapacity, region):
		self.maxCapacity = maxCapacity
		self.region = region
		self.expiryTime = int(time.time()) + EXPIRES_AFTER
		# We use an OrderedDict instead of a normal dictionary because in 
		# our case, the min key search in a dict is O(n) whereas a key search
		# in an OrderedDict is O(1). This is b/c the oldest used item will 
		# be at the bottom of the OrderedDict.
		self.cache = collections.OrderedDict() # (key,value) = (itemName, timeAdded)

	""" returns value corresponding to key

	If key is found, pops out the (key,value) pair from cache, then reinserts it so it becomes
	the most recent item.
	"""
	def get(self, key):
		try:
			value = self.cache.pop(key)
			self.cache[key] = value
			return value
		except KeyError:
			return -1

	""" insert new (key, value) pair

	If pair already exists, make it the most recent item.
	If cache is full, pops out last (key, value) pair, then inserts new pair.
	"""
	def set(self, key, value):
		try:
			self.cache.pop(key)
		except KeyError:
			if len(self.cache) >= self.maxCapacity:
				self.cache.popitem(last=False)
		self.cache[key] = value
		