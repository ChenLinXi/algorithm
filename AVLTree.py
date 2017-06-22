#
#	AVLTree.py inherited from BinarySearchTree.py and BinaryTree.py
#	Author: Jason Chen
#	Created Time: 2017/6/22 15:00
#	Functions:
#		1. right rotate
#		2. left rotate
#		3. left and right rotate
#		4. right and left rotate
#	
#	balanceFactor = height(leftSubTree) - height(rightSubbbbTree)
#	left-heavy:  balanceFactor = 1
#	right-heavy: balanceFactor = -1
#	balance:	  balanceFactor = 0
#


import BinarySearchTree as BST
import BinaryTree as BT

class AVLTreeNode(BT.BinaryTreeNode):
	
	__slots__ = {'data','left','right','height'}

	def __init__(self,data=0,left=0,right=0,height=0):
		BT.BinaryTreeNode.__init__(self,data,left,right)
		self.height = height


class AVLTree(BST.BinarySearchTree):

	# left rotate
	def leftRotate(self, treenode):
		node = treenode.right
		treenode.right = node.left
		node.left = treenode
		node.height = self.getHeight(node)
		treenode.height = self.getHeight(treenode)
		return node

	# right rotate
	def rightRotate(self, treenode):
		node = treenode.left
		treenode.left = node.right
		node.right = treenode
		node.height = self.getHeight(node)
		treenode.height = self.getHeight(treenode)
		return node

	# left and right rotate
	# 1. left rotate treenode's child node
	# 2. right rotate treenode
	def left2RightRotate(self, treenode):
		node = treenode.left
		treenode.left = self.leftRotate(node)
		return self.rightRotate(treenode)

	# right and left rotate
	# 1. right rotate treenode's child node
	# 2. left rotate treenode 
	def right2LeftRotate(self, treenode):
		node = treenode.right
		treenode.right = self.rightRotate(node)
		return self.leftRotate(treenode)

	def insert(self, data):
		self.root = self.insertNode(self, root, data)

	def insertNode(self, treenode, data):

		if not treenode:
			node = AVLTreeNode(data=data)
			node.height = self.getHeight(node)
			return node

		# direction = 0: delete left
		# direction = 1: delete right
		direction = 0 if treenode.data > data else 1
		treenode[direction] = self.insertNode(treenode[direction], data)
		leftHeight = 0 if not treenode.left else self.getHeight(treenode.left)
		rightHeight = 0 if not treenode.right else self.getHeight(treenode.right)

		if not leftHeight - rightHeight < 2:
			node = treenode.left

			# 1. right rotate when 'left left'
			# 2. left2Right when 'left right'
			return self.rightRotate(treenode) if self.getHeight(node.left) > self.getHeight(node.left) else self.left2RightRotate(treenode)  

		elif not rightHeight - leftHeight < 2:

			# 1. left rotate when 'right right'
			# 2. right2Left when 'right left'
			return self.leftRotate(treenode) if self.getHeight(node.right) > self.getHeight(node.left) else self.right2LeftRotate(treenode)			

		else:
			return treenode

	# delete 'data' beginning with 'treenode'
	def delNode(self, treenode, data):

		if not treenode.left and not treenode.right:
			return 'leaf'

		if treenode.data is data:
			if treenode.left and treenode.right:
				rightnode = treenode.right
				rightparent = rightnode

				while rightnode.left:
					rightparent = rightnode
					rightnode = rightnode.left

				treenode.data = rightnode.data
				if self.delNode(rightnode, rightnode.data) is 'leaf':
					rightparent.left = None

			else:
				# direction = 0: delete left
				# direction = 1: delete right
				direction = 0 if treenode.left else 1
				treenode.data = treenode[direction].data
				if self.delNode(treenode[direction], data) is 'leaf':
					treenode[direction] = None

		else:
			parent = treenode
			direction = 0 if treenode.data > data else 1
			treenode = parent[direction]
			if self.delNode(treenode, data) is 'leaf':
				parent[direction] = None

		# delete treenode and reset
		leftHeight = 0 if not treenode.left else self.getHeight(treenode.left)
		rightHeight = 0 if not treenode.right else self.getHeight(treenode.right)

		if not leftHeight - rightHeight < 2:
			node = treenode.left

			# 1. right rotate when 'left left'
			# 2. left2Right when 'left right'
			self.rightRotate(treenode) if self.getHeight(node.left) >  self.getHeight(node.left) else self.left2RightRotate(treenode)
			return 'node'
		elif not rightHeight - leftHeight < 2:
			node = treenode.right
			self.leftRotate(treenode) if self.getHeight(node.right) > self.getHeight(node.left) else self.right2LeftRotate(treenode)
			return 'node'
		else:
			return 'node'

def main():  
    bt = AVLTree()  
    n8 = AVLTreeNode(8,0,0)  
    n6 = AVLTreeNode(6,0,0)  
    n15 = AVLTreeNode(15,0,0)  
    n13 = AVLTreeNode(13,0,0)  
    n11 = AVLTreeNode(11,0,0)  
    n9 = AVLTreeNode(9,0,0)  
    n5 = AVLTreeNode(5,0,n6)  
    n3 = AVLTreeNode(3,0,0)  
    n1 = AVLTreeNode(1,0,0)  
  
    n7 = AVLTreeNode(7,n5,n8)  
    n14 = AVLTreeNode(14,n13,n15)  
    n10 = AVLTreeNode(10,0,n11)  
    n12 = AVLTreeNode(12,n10,n14)  
    n2 = AVLTreeNode(2,n1,n3)  
    n4 = AVLTreeNode(4,n2,n7)  
    n9 = AVLTreeNode(9,n4,n12)  
  
    bt.root = n9  
  
    bt.delNode(bt.root,12)  
    bt.midOrder(bt.root)  
  
##    for i in range(1,16):  
##        exec("node = bt.findNode(bt.root,"+str(i)+")")  
##        print str(i)+':'+str(node.height)  
  
    pass  
  
if __name__ == '__main__':  
    main()  
