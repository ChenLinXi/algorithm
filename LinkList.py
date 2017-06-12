#
#	LinkList.py 
#	Coding of Robust
#	updated time: 17/6/12 14:00
#	Author: Jason Chen at 369575409@qq.com
#

#!/usr/bin/python
#coding=utf-8

class Node(object):
	def __init__(self, value, p = 0):
		self.data = value
		self.next = p

class LinkList(object):
	def __init__(self):
		self.head = 0

	# build-in functions 'getitem' to get value from list based on key
	# params: key(index of the list node)
	# return: value of special key
	def __getitem__(self, key):

		if self.is_empty():
			print 'linklist is empty'
			return

		elif key < 0 or key > self.getlength():
			print 'the given key is error'
			return

		else:
			return self.getitem(key)

	# build-in functions 'setitem' to set key's value in list
	# params: key, value
	# return: self.insert(key)
	def __setitem__(self, key, value):

		if self.is_empty():
			print 'linklist is empty'
			return

		elif key < 0 or key > self.getlength():
			print 'the given key is error'
			return

		else:
			self.delete(key)
			return self.insert(key)

	# FUNCTIONS: initial link list with given data(array)
	# PARAMS: data means an array contains lots of elements
	def initlist(self, data):

		if len(data) == 0:
			print 'the given data is error'
			return

		self.head = Node(data[0])
		p = self.head

		for i in data[1:]:
			node = Node(i)
			p.next = node
			p = p.next	

	# FUNCTIONS: get the length of link list
	def getlength(self):

		p = self.head
		length = 0
		while p != 0:
			length += 1
			p = p.next

		return length

	# FUNCTIONS: check the list whether it is null based on list length
	def is_empty(self):

		if self.getlength() == 0:
			return True
		else:
			return False

	# FUNCTIONS: clear list
	def clear(self):

		self.head = 0

	# FUNCTIONS: append node to list
	def append(self, item):
		
		q = Node(item)
		if self.head == 0:
			self.head = q
		else:
			p = self.head
			while p.next != 0:
				p = p.next
			# when p.next == 0
			# append the Node(item) behind of the list
			p.next = q

	# FUNCTIONS: get the Node'value based on index
	def getitem(self, index):

		if self.is_empty():
			print 'LinkList is empty.'
			return
		counter = 0
		p = self.head

		while p.next != 0 and counter < index:
			p = p.next
			counter += 1

		if counter == index:
			return p.data

		else:
			print 'target is not exist！'

	# FUNCTIONS: insert Node to List based on index
	# PARAMS: index, item
	# RETURN: NULL
	def insert(self, index, item):
		if self.is_empty() or index < 0 or index > self.getlength():
			print 'LinkList is empty.'
			return

		if index == 0:
			q = Node(item, self.head)

			self.head = q

		p = self.head
		post = self.head
		counter = 0
		while p.next != 0 and counter < index:
			post = p
			p = p.next
			counter += 1

		if index == counter:
			q = Node(item, p)
			post.next = q
			q.next = p

	# FUNCTIONS: delete node from link list based on index
	def delete(self, index):

		if self.is_empty() or index < 0 or index > self.getlength():
			print 'LinkList is empty.'
			return

		if index == 0:
			q = Node(item, self.head)
			self.head = q

		p = self.head
		post = self.head
		counter = 0
		while p.next != 0 and counter < index:
			post = p
			p = p.next
			counter += 1

		if index == counter:
			post.next = p.next

	# FUNCTIONS: get the first index from link list based on value
	# PARAMS: value
	# RETURN: index
	def index(self, value):

		if self.is_empty():
			print 'LinkList is empty.'
			return

		p = self.head
		counter = 0
		while p.next != 0 and not p.data == value:
			p = p.next
			counter += 1

		if p.data == value
			return counter
		else:
			return -1

# FUNTIONS: here goes the link list test
def main():
	l = LinkList()
	l.initlist([1,2,3,4,5])
	print l.getitem(4)
	l.append(6)
	print l.getitem(5)

	l.insert(4, 40)
	print l.getitem(3)
	print l.getitem(4)
	print l.getitem(5)

	l.delete(5)
	print l.getitem(5)

	l.index(5)

if __name__ == "__main__":
	main()
