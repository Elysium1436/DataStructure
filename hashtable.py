class LinearMap:

	def __init__(self):
		self.items=[]


	def add(self,k,v):
		self.items.append((k,v))

	def get(self,k):
		for t,v in self.items:
			if t==k:
				return v

		raise KeyError




class BetterMap:

	def __init__(self,n=100):
		self.bmap=[]
		for i in range(n):
			self.bmap.append(LinearMap())

	def findmap(self,k):
		i=hash(k)%len(self.bmap)
		return self.bmap[i]

	def addmap(self, k, v):
		m=self.findmap(k)
		m.add(k,v)

	def get(self,k):
		m=self.findmap(k)
		return m.get(k)

class HashTable:

	def __init__(self):
		self.htable=BetterMap(50)
		self.num=0



	def add(self, k, v):
		if self.num==len(self.htable.bmap):
			self.resize()

		self.htable.addmap(k,v)
		self.num+=1


	def get(self, k):
		return self.htable.get(k)

	def resize(self):
		newMap=BetterMap(self.num*2)

		for m in self.htable.bmap:
			for k,v in m.items:
				newMap.add(k,v)


		self.htable=newMap



h=HashTable()

h.add(1,"yeet")
h.add(2,"yote")
h.add(3,"yate")
h.add(4,"yute")

print([h.get(i) for i in range(1,5)])