#  镜像二叉树解法：
#  
#  1) 逐步递归比较二叉树节点，满足如下条件即可： 
#  node1.left = node2.right and node1.right = node2.left
#  
#  2) 将普通二叉树补全成完全二叉树
#  (即为面试时的答题思路，可以避免先序、中序、倒序遍历带来的二叉树不一致性)
#  
#  Updated time: 20:00 2017/6/9

# 方法一：逐次迭代递归比较（关键代码）
import os

class Node:
	def __init__(self, left, right, value):
		self.left = left
		self.right = right
		self.value = value

class Tree:
	def __init__(self):
		self.root = Node()
		self.root.lchild = Node()
		self.root.rchild = Node()

def isSymmetric(root) {
	if root != NULL:
		return Symmetric(root.lchild, root.rchild)
}

# 逐次比较节点的值
def Symmetric(root.lchild, root.rchild):
	if root.lchild != NULL and root.rchild != NULL:
		return true
	if root.lchild != NULL or root.rchild != NULL:
		return false
	if root.lchild.value == root.rchild.value:
		return Symmetric(root.lchild.lchild, root.rchild.rchild) and Symmetric(root.lchild.rchild, root.rchild.lchild)
	

########
#分割线#
########

# 方法二： 补全普通二叉树，以前序遍历存储树的信息
import os

# flag 补全二叉树为完全二叉树参数
# lArray/rArray 记录左子树、由子树数据
flag = 'NULL'
lArray = []
rArray = []

class Node:
	def __init__(self, left, right, value):
		self.left = left
		self.right = right
		self.value = value

class Tree:
	def __init__(self):
		self.root = Node()
		self.root.lchild = Node()
		self.root.rchild = Node()

def checkNode(node):
	if node.lchild == NULL and node.right == NULL:
		return 0
	elif node.lchild == NULL and node.right != NULL:
		return 1
	elif node.lchild != NULL and node.right == NULL:
		return 2
	else:
		return 3

# 如果节点为空，用flag补全成完全二叉树
def encoder(root.lchild, root.rchild):
	if root.lchild.value == root.rchild.value:
		# 左子树
		switch(checkNode(root.lchild)){
			case 0:
				lArray.append(flag)
				encoder(root.lchild.lchild, root.lchild.rchild)
				lArray.append(flag)
			case 1:
				lArray.append(flag)
				encoder(root.lchild.lchild, root.lchild.rchild)
				lArray.append(root.lchild.rchild.value)
			case 2:
				lArray.append(root.lchild.lchild.value)
				encoder(root.lchild.lchild, root.lchild.rchild)
				lArray.append(flag)
			case 3:
				lArray.append(root.lchild.lchild.value)
				encoder(root.lchild.lchild, root.lchild.rchild)
				lArray.append(root.lchild.rchild.value)
		}

		# 右子树
		switch(checkNode(root.rchild)){
			case 0:
				rArray.append(flag)
				encoder(root.rchild.lchild, root.rchild.rchild)
				rArray.append(flag)
			case 1:
				rArray.append(flag)
				encoder(root.rchild.lchild, root.rchild.rchild)
				rArray.append(root.rchild.rchild.value)
			case 2:
				rArray.append(root.rchild.lchild.value)
				encoder(root.rchild.lchild, root.rchild.rchild)
				rArray.append(flag)
			case 3:
				rArray.append(root.rchild.lchild.value)
				encoder(root.rchild.lchild, root.rchild.rchild)
				rArray.append(root.rchild.rchild.value)
		}
	else:
		return

# 基于先序遍历检查两个数组之间的关系
def isFamilar(lArray, rArray):
	llen = len(lArray)
	rlen = len(rArray)
