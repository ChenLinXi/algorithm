#
#	BinarySearchTree.py
#	Inherit from BinaryTree.py
#	Author: Jason Chen
#	CreatedTime: 2017/6/22 14:30
#

import BinaryTree as BTree

# inherit from Binary tree
# BinarySearchTree obey this rule(middle order): 
# 	root.left.data < root.data < root.right.data

class BinarySearchTree(BTree.BinaryTree):

	def __init__(self, root=0, count=0, height=0):
		BTree. BinaryTree.__init__(self, root, count, height)

	# params: treenode(node to be inserted to binary tree)
	def insertNode(self, treenode):

		if treenode == 0:
			return
		if self.root == 0:
			self.root = treenode
			return
		self.count += 1
		currentNode = self.root

		# 1.compare treenode with root.left
		# 2.compare treenode with root.right
		# 3.insert treenode to Binary Search Tree
		while currentNode:

			if currentNode.data < treenode.data:
				if currentNode.right == 0:
					currentNode.right = treenode
					return
				else:
					currentNode = currentNode.right

			elif currentNode.data > treenode.data:
				if currentNode.left == 0:
					currentNode.left = treenode
					return
				else:
					currentNode = currentNode.left

	# params: currentNode, data
	# funcs:  delete 'data' from binary tree beginning with 'currentNode'
	def delNode(self, currentNode, data):

		if not currentNode.left and not currentNode.right:
			currentNode.data = None
			return 'leaf'

		# currentNode is the one to be deleted in Binary Tree
		# percUp the child node
		if currentNode.data is data:

			# current node has left and right child
			# percUp left Child to top
			if currentNode.left and currentNode.right:
				# 1. record the current node
				rightNode = currentNode.right
				rightParent = rightNode

				# 2. percUp util the end
				while rightNode.left:
					rightParent = rightNode
					rightNode = rightNode.left

				# 3. when left loop finished, goes on right loop
				currentNode.data = rightNode.data
				if self.delNode(rightNode, rightNode.data) is 'leaf':
					rightParent.left = None

				return 'node'

			# current node has left or right child
			else:
				direction = 0 if currentNode.left else 1
				node = currentNode[direction]

		else:

			parent = currentNode
			direction = 0 if currentNode.data > data else 1
			currentNode = parent[direction]

			if self.delNode(currentNode, data) is 'leaf':
				parent[direction] = None

# example:
def main():  
    n8 = BTree.BinaryTreeNode(8,0,0)  
    n6 = BTree.BinaryTreeNode(6,0,0)  
    n15 = BTree.BinaryTreeNode(15,0,0)  
    n13 = BTree.BinaryTreeNode(13,0,0)  
    n11 = BTree.BinaryTreeNode(11,0,0)  
    n9 = BTree.BinaryTreeNode(9,0,0)  
    n5 = BTree.BinaryTreeNode(5,0,0)  
    n3 = BTree.BinaryTreeNode(3,0,0)  
    n1 = BTree.BinaryTreeNode(1,0,0)  
  
    n7 = BTree.BinaryTreeNode(7,n5,n8)  
    n14 = BTree.BinaryTreeNode(14,n13,n15)  
    n10 = BTree.BinaryTreeNode(10,0,n11)  
    n12 = BTree.BinaryTreeNode(12,n10,n14)  
  
  
    n2 = BTree.BinaryTreeNode(2,n1,n3)  
    n4 = BTree.BinaryTreeNode(4,n2,n7)  
    n9 = BTree.BinaryTreeNode(9,n4,n12)  
  
    root = n9  
    bt = BinarySearchTree(root)  
    bt.insertNode(n6)  
  
    bt.delNode(root,12)  
    bt.delNode(root,9)  
    bt.midOrder(bt.root)  
  
  
  
##    bt = BinarySearchTree()  
##    for i in range(1,16):  
##        exec("n"+str(i)+" = BTree.BinaryTreeNode("+str(i)+",0,0)")  
##        exec("bt.insertNode(n"+str(i)+")")  
##    bt.delNode(4)  
##    bt.delNode(5)  
##    bt.delNode(6)  
##    bt.preOrder(bt.root)  
  
if __name__ == '__main__':  
    main()  
