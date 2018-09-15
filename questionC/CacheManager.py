## The idea was to have a singletion CacheManager that had access to all caches
## and would've handled data transfer, finding the closest cache geographically,
## and perhaps expiring caches.

## After 3 hours and 50 minutes, I realized I could've 
## used the memcached package which I think would've made my life easier.


from . import Cache

class CacheManager(object):
	"""A singleton that manages caches their interaction"""

	# from https://gist.github.com/pazdera/1098129
	@staticmethod
	def getInstance():
		""" static access method """
		if CacheManager.__instance == None:
			CacheManager()
		return CacheManager.__instance 

	__instance = None

	def __init__(self):

		if CacheManager.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			CacheManager.__instance = self

		self.cacheDict = {} # Store caches as (region, Cache) pair
		# Assumes there's only 1 cache per region
		# 
		
	""" return dictionary containing (region, Cache) pairs
	"""
	def getCacheDict(self):
		return self.cacheDict

	"""create new cache and add it to CM's set
	"""
	def createCache(self, maxCapacity, region):
		newCache = Cache(maxCapacity, region)
		self.cacheDict[region] = newCache

	"""transfer data between 2 caches
	
	"""
	def transferData(self, region1, region2):
		cache1 = self.getCacheDict[region1]
		cache2 = self.getCacheDict[region2]
		## did not have time to implement this
		

	def nearestCache(self, userLocation):
		pass
		## did not have time to implement this



if __name__ == '__main__':
	s1 = CacheManager.getInstance()

	s1.createCache(5, "Montreal")
	s1.createCache(5, "Vancouver")
	print (len(s1.getCacheDict()))

	s2 = CacheManager.getInstance()
	print (len(s1.getCacheDict()))