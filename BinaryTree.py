#
# BinaryTree.py
# Author: Jason Chen
# Created Time: 2017/6/22
# 
# Functions: 
# 	1.build Normol Binary Tree
# 	2.convert Binary Tree to Max Heap
# 	3.build Max Tree 
#	



class BinaryTreeNode(object):

	__slots__ = ['data', 'left', 'right']

	def __init__(self, data=0, left=0, right=0):
		self.data = data
		self.left = left
		self.right = right

	def __getitem__(self, key):
		return self.left if key == 0 else self.right

	def __setitem__(self. key, data):

		if key == 0:
			self.left = data
		elif key == 1:
			self.right = data


class BinaryTree(object):

	__slots__ = ['root', 'count', 'height']

	def __init__(self, root=0, count=0, height=0):
		self.root = root
		self.count = 0	# node number
		self.height = 0 # tree height

	def __del__(self):
		pass

	# find node
	def findNode(self, treenode, data):
		# robont
		if not treenode:	# check whether node is none
			return

		if treenode.data == data:	# find node based on data
			return treenode	
		else:
			treenodeLeft = self.findNode(treenode.left, data)
			treenodeRight = self.findNode(treenode.right, data)
			return treenodeLeft if not treenodeLeft else treenodeRight


	# find node's parent
	def findParent(self, treenode, data):
		
		if not treenode:
			return

		if self.childCount(treenode) == 'twins':
			if treenode.right.data == data or treenode.left.data == data:
				return treenode
			else:
				treenodeLeft = self.findParent(treenode.left, data)
				treenodeRight = self.findParent(treenode.right, data)
				return treenodeLeft if treenodeLeft else treenode.right
		elif self.childCount(treenode) is 'left' or 'right':
			node = treenode.left if treenode.left else treenode.right
			if node.data == data:
				return treenode
			else:
				return self.findParent(node, data)
		else:
			return

	
	# find treenode's leaf
	def findLeaf(self, treenode):
		
		if not treenode:
			return

		if self.childCount(treenode) == 'none':
			print treenode.data
		else:
			self.findLeaf(treenode.left)
			self.findLeaf(treenode.right)


	# check node whether has child node
	# return: 'none', 'right', 'left', 'twins'
	def childCount(self, treenode):
		
		if not treenode.left and not treenode.right:
			return 'none'
		elif not treenode.left:
			return 'right'
		elif not treenode.right:
			return 'left'
		else:
			return 'twins'


	# create a binary tree
	def create(self):
		
		temp = input('enter a value:')
		if temp is 99:
			return
		treenode = BinaryTreeNode(data = temp)
	
		if not self.root:
			self.root = treenode
			treenode.left = self.create()
			treenode.right = self.create()
			return treenode


	# calculate node's number
	def nodeCount(self, treenode):
		
		if treenode:
			self.count += 1
			self.nodeCount(treenode.left)
			self.nodeCount(treenode.right)


	# pre order
	# (root, root.left, root.right)
	def preOrder(self, treenode):
		
		if not treenode:
			return
		print treenode.data
		self.preOrder(treenode.left)
		self.preOrder(treenode.right)


	# middle order
	# (root.left, root, root.right)
	def midOrder(self, treenode):
		
		if not treenode:
			return
		self.midOrder(treenode.left)
		print treenode.data
		self.midOrder(treenode.right)


	# after order
	# (root.left, root.right, root)
	def aftOrder(self, treenode):
		
		if not treenode:
			return
		self.aftOrder(treenode.left)
		self.aftOrder(treenode.right)
		print treenode.data


	# get treenode's child height
	def getHeight(self, treenode):

		if not treenode:
			return 0
		elif self.childCount(treenode) == 'none':
			return 1

		left = self.getHeight(treenode.left)
		right = self.getHeight(treenode.right)
		return left+1 if left>right else right+1


	# convert binary tree to max heap
	def MaxHeap(self, treenode):

		if not treenode is 0:
			return
		if self.childCount(treenode) == 'none':
			return
		elif self.childCount(treenode) == 'left' or 'right':
			# when treenode has only one child node
			# check child node's data and treenode.data
			# percUp the bigger number
		
			node = treenode.left if treenode.left else treenode.right
			if treenode.data < node.data:
				treenode.data, node.data = node.data, treenode.data
			self.MaxHeap(node)
		else:
			# when treenode has left and right child node 
			# and the treenode.data is smaller than the childs
			# here goes two situations
		
			if treenode.right.data > treenode.left.data and treenode.data < treenode.right.data:
				treenode.data, treenode.right.data = treenode.right.data, treenode.data
			elif treenode.right.data < treenode.left.data and treenode.data < treenode.left.data:
				treenode.data, treenode.left.data = treenode.left.data, treenode.data

			self.MaxHeap(treenode.left)
			self.MaxHeap(treenode.right)


	# build max tree based on after order
	def BuildMaxTree(self, treenode):

		if not treenode:
			return
		self.BuildMaxTree(treenode.left)
		self.BuildMaxTree(treenode.right)
		self.MaxHeap(treenode)


# example goes here:
def main():
	n10 = BinaryTreeNode(10, 0, 0)
	n9 = BinaryTreeNode(9, 0, 0)
	n3 = BinaryTreeNode(3, n9, n10)
	n8 = BinaryTreeNode(8, 0, 0)
	n14 = BinaryTreeNode(14, 0, 0)
	n7 = BinaryTreeNode(7, 0, 0)
	n16 = BinaryTreeNode(16, n7, 0)
	n2 = BinaryTreeNode(2,n14,n8)  
    n1 = BinaryTreeNode(1,n2,n16)  
    root = BinaryTreeNode(4,n1,n3) 

    bt = BinaryTree(root)
    print bt.findParent(bt.root, n3.data).data

    pass

if __name__ == "__main__":
	main()
