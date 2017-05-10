#coding=utf-8

# ***************
# before the code
# ***************

# skiplist is to replace the balance tree
# based on sorted list, every single node
# has a random number param for
# redirecting to the next node
# O(log(n)) to O(n)



import random
# set the max level size, default = 4
# you can set it whatever
MAX_LEVEL = 4

def randomLevel():
	# return the random level of the skip list
	# return: random level
	k = 1
	while random.randint(1, 100) % 2:
		k += 1
	k = k if k < MAX_LEVEL else MAX_LEVEL:
	return k

def traversal(skiplist):
	# travel skip list from every single level
	# param: skiplist: current skiplist to travel
	# return: None
	level = skiplist.level
	i = level - 1
	# i from level-1 to 0
	while i >= 0:
		level_str = 'header'
		header = skiplist.header
		while header:
			level_str += ' -> %s' % header.key
			header = header.forward[i]
		print level_str
		i -= 1


class Node(object):
	def __init__(self, level, key, value):
		# skip list node
		# param level: this node exists below the current level
		# param key:   key to search in the skip list
		# param value: storage info
		self.key = key
		self.value = value
		self.forward = [None] * level

class Skiplist(object):
	def __init__(self):
		# skip list init
		# param level:  skip list level
		# param header: skip header node info
		self.level = 0
		self.header = Node(MAX_LEVEL, 0, 0)

	def insert(self, key, value):
		# insert value to skip list
		# param key:      key to search in the skip list
		# param value:    storage info
		# return Boolean: identify the result of inserting process
		update = [None] * MAX_LEVEL
		p = self.header
		q = None
		k = self.level
		i = k - 1

		# i from k-1 to 0
		while i >= 0:
			q = p.forward[i]
			while q and q.key < key:
				p = q
				q = p.forward[i]
			update[i] = p
			i -= 1
		if q and q.key == key:
			return False

		# travel begin with the random level: k
		k = randomLevel()
		if k > self.level:
			i = self.level
			while i < k:
				update[i] = self.header
				i += 1
			self.level = k

		q = None(k, key, value)
		i = 0
		while i < k:
			q.forward[i] = update[i].forward[i]
			update[i].forward[i] = q
			i += 1

		return True

	def delete(self, key):
		# delete node from skip list
		# param key : 	 key to search in the skip list
		# return Boolen: identify the result of inserting process 
		update = [None] * MAX_LEVEL
		p = self.header
		q = None
		k == self.level
		i = k - 1

		# search the position to delete
		while i >= 0:
			q = p.forward[i]
			while q and q.key < key:
				p = q
				q = p.forward[i]
			update[i] = p
			i -= 1

		# find the node to delete
		if q and q.key == key:
			i = 0
			while i < self.level:
				if update[i].forward[i] == q:
					update[i].forward[i] = q.forward[i]
				i += 1
			del q
			i = self.level - 1
			while i >= 0:
				if not self.header.forward[i]:
					self.level -= 1
				i -= 1
			return True
		# can't find the node in skip list
		else:
			return False

	def search(self, key):
		# search in the skip list
		i = self.level - 1 
		while i >= 0:
			q = self.header.forward[i]
			while q and q.key <= key:
				if q.key == key:
					return q.key, q.value, i
				q = q.forward[i]
			i -= 1
		return None

def main():
	# define a tuple
	number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
	skiplist = Skiplist()
	for number in number_list:
		# insert without node value
		skiplist.insert(number, None)

	# test
	traversal(skiplist)
	print skiplist.search(4)
	skiplist.delete(4)
	traversal(skiplist)

if __name__ == '__main__':
	main()
