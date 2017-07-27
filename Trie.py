#!/usr/bin/env python
#coding: utf-8

#	trie.py 实现前缀树排序的功能
#	分为以下几部分组成：
#	1. 树节点
#	2. 前缀树
#	3. 插入字符串

# Node: 定义trie的节点
# @c :节点存储的单个字符
# @word: 节点存储的词, 避免相同前缀引起的冲突
class Node(object):
	def __init__(self, c=None, word=None):
		self.c = c 
		self.word = word
		self.childs = []

# Trie: 定义前缀树trie结构
class Trie(object):
	# init: 引用根节点
	def __init__(self):
		self.root = Node()

	# setWords: Trie树迭代赋值
	def setWords(self, words):
		for word in words:
			self.add(word)

	# find: 查找字符插入位置
	# @node: 当前节点
	# @c: 待插入字符
	# return: 返回待插入字符在当前节点的哪一个子节点中
	def find(self, node, c):
		childs = node.childs
		_len = len(childs)
		if _len == 0:
			return -1
		for i in range(_len):
			if childs[i].c == c:
				return i
		return -1

	# add: 往Trie中添加字符串
	# @word: 待插入的字符串
	def add(self, word):
		node = self.root
		# 迭代插入字符串的字符
		for c in word:
			pos = self.find(node, c)
			# 字符不存在
			if pos < 0:
				# 在原有节点中添加子节点
				node.childs.append(Node(c))
				# 添加子节点后将子节点按照字典顺序重新排序
				node.childs = sorted(node.childs, key=lambda child: child.c)
				# 找到排序后新节点的位置
				pos = self.find(node, c)
			node = node.childs[pos]
		# 记录当前节点插入的字符串
		node.word = word

	# preOrder: 先序遍历输出
	# @node: 遍历的起始节点
	def preOrder(self, node):
		results = []
		if node.word:
			results.append(node.word)
		for child in node.childs:
			# x = [1, 2, 3]
			# x.extend([4, 5])
			# x = [1, 2, 3, 4, 5]
			results.extend(self.preOrder(child))
		return results

if __name__ == "__main__":
	words = ['python', 'function', 'php', 'food', 'kiss', 'perl', 'goal', 'go', 'golang', 'easy']
	trie = Trie()
	trie.setWords(words)
	result = trie.preOrder(trie.root)
	print '原始字符串数组： %s' % words
	print 'Trie树排序结果： %s' % result
	words.sort()
	print 'Python内置Sort: %s' % words
