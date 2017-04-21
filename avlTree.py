#coding=utf-8

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

class AVLTree(object):
    def __init__(self):
        self.root = None

    def find(self, key):
        if self.root is None:
            return None
        else:
            return self._find(key, self.root)

    def _find(self, key, node):
        if node is None:
            return None
        elif key < node.key:
            return self._find(key, self.left)
        elif key > node.key:
            return self._find(key, self.right)
        else:
            return node

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)

    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node

    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)

    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    # rotate rules:
    # insert a node may break the balance of the tree, we call the first node "K"
    # "K" has left and right child node, those height count 2
    # 1. insert to "K"'s left child's left tree, rotate once
    # 2. insert to "K"'s left child's right tree, rotate twice
    # 3. insert to "K"'s right child's left tree, rotate twice
    # 4. insert to "K"'s right child's right tree, rotate once

    # node's child height counts 2
    # single left rotate
    # node.left, node = node, node.right
    # eg:
    # node.key = 35, node.left.key = 30, node.left.left.key = 25
    # Rotate to: node.key = 30, node.left.key = 25, node.right.key = 35
    def singleLeftRotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height) + 1
        return k1

    # node's child height counts 2
    # single right rotate
    # node.right.left, node.right = node.right, node
    def singleRightRotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    # double left rotate
    # node.right.left, node.right, node = node, node.right, node.left
    # 1.singleRightRotate
    # 2.singleLeftRotate
    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)

    # double right rotate
    # node.left.right.left, node.left.right.right, node.left.right = node.left.right, node.right.left, node.right
    # 1. singleLeftRotate
    # 2. singleRightRotate
    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    def put(self, key):
        if not self.root:
            self.root = None(key)
        else:
            self.root = self._put(key, self.root)

    def _put(self, key, node):
        if node is None:
            node = Node(key)
        elif key < node.key:
            # 1,key is smaller than node.key
            node.left = self._put(key, node.left)
            # after putting, check the children's height
            if (self.height(node.left) - self.height(node.right)) == 2:
                # if key is smaller then node.left.key, then single left rotate
                if key < node.left.key:
                    node = self.singleLeftRotate(node)
                # key is bigger than node.left.key, then double left rotate
                else:
                    node = self.doubleLeftRotate(node)

        elif key > node.key:
            # 2.key is bigger than node.key
            node.right = self._put(key, node.right)
            # after putting, check the children's height
            if (self.height(node.right) - self.height(node.left)) == 2:
                # key is smaller than node.right.key, so double right rotate
                if key < node.right.key:
                    node = self.doubleRightRotate(node)
                # if key is bigger than node.right.key, then single right rotate
                else:
                    node = self.singleRightRotate(node)
        # reset node height
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        # return node
        return node

    def delete(self, key):
        self.root = self.remove(key, self.root)

    # 1.current node has no child, remove it directly
    # 2.current node has one left child or right child, do single left or right rotate
    # 3.current node is the one which will be removed, but it has left&right child's tree
    #   if right child tree's height is bigger than the other, take the one which is smallest in right child tree
    #   and take place of the current node;
    #   else if the left child tree's height is bigger than the other, take the one which is biggest in left child tree
    #   and take place of the current node
    #   after remove and rotate, remember reset node's height
    # 4. current node is not the one to be removed, then do left or right Recursive work and check the balance of tree
    def remove(self, key, node):
        if node is None:
            raise KeyError,'Error, key not in tree'

        # key is smaller than node.key, do left Recursive work
        elif key < node.key:
            node.left = self.remove(key, node.left)
            # after Recursive, check node's child height
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightRotate(node)
            # reset node height
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        # key is bigger than node key, do right Recursive work
        elif key > node.key:
            node.right = self.remove(key, node.right)
            # after Recursive, check node's child height
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        # node has left&right child
        elif node.left and node.right:
            if node.left.height <= node.right.height:
                minNode = self._findMin(node.right)
                node.key = minNode.key
                node.right = self.remove(node.key, node.right)
            else:
                maxNode = self._findMax(node.left)
                node.key = maxNode.key
                node.left = self.remove(node.key, node.left)
            # reset node height
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        else:
            if node.right:
                node = node.right
            else:
                node = node.left

        return node
