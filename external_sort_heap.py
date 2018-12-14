# a heap structure designed for external sort

import random
import sys
import collections

item = collections.namedtuple('item', ['listname', 'index', 'value'])

class Heap:
	def __init__(self):
	    self.h = []
	    self.currsize = 0

	def leftChild(self,i):
		if 2*i+1 < self.currsize:
			return 2*i+1
		return None

	def rightChild(self,i):
		if 2*i+2 < self.currsize:
			return 2*i+2
		return None

	def maxHeapify(self,node):
		if node < self.currsize:
			m = node
			lc = self.leftChild(node)
			rc = self.rightChild(node)
			if lc is not None and self.h[lc].value < self.h[m].value:
				m = lc
			if rc is not None and self.h[rc].value < self.h[m].value:
				m = rc
			if m!=node:
				temp = self.h[node]
				self.h[node] = self.h[m]
				self.h[m] = temp
				self.maxHeapify(m)


	def getTop(self):
		if self.currsize >= 1:
			me = self.h[0]
			temp = self.h[0]
			self.h[0] = self.h[self.currsize-1]
			# self.h[self.currsize-1] = temp
			del self.h[self.currsize-1]
			self.currsize -= 1
			self.maxHeapify(0)
			return me
		return None

	def insert(self,data):
		self.h.append(data)
		curr = self.currsize
		self.currsize+=1
		while self.h[curr].value < self.h[curr//2].value:
			temp = self.h[curr//2]
			self.h[curr//2] = self.h[curr]
			self.h[curr] = temp
			curr = curr//2

	def display(self):
		print(self.h)

def main():

	listsize = 1000
	listcount = 1000
	l = [[random.randrange(1, 10000) for i in range(listsize)] for index in range(listcount)]
	list(map(lambda a : a.sort(), l))

	h = Heap()
	for i in range(len(l)):
		h.insert(item(i, 0, l[i][0]))
	output = []
	flag = 0
	while flag < listcount * listsize:
		temp = h.getTop()
		output.append(temp.value)
		if temp.index < listsize - 1:
			h.insert(item(temp.listname, temp.index+1, l[temp.listname][temp.index+1]))
		flag += 1
	print(len(output))


if __name__=='__main__':
	main()

