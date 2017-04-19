#coding=utf-8

class BinarySearchTree(object):
    def __init__(self, key):
        # 1.BinarySearchTree rule: node.left < node.key < node.right
        self.key = key
        self.left = None
        self.right = None

    def find(self, x):
        # 1.find current node
        if x == self.key:
            return self
        # 2.find left child node and check self.left whether exists
        elif x < self.key and self.left:
            return self.left.find(x)
        # 3.find right child node and check self.right whether exists
        elif x > self.key and self.right:
            return self.right.find(x)
        # 4.None: can't find
        else:
            return None

    def findMin(self):
        # 1.left child is lower than right child
        # 2.find left child node till the end
        if self.left:
            return self.left.findMin()
        else:
            return self

    def findMax(self):
        # 1.right child is bigger than left child
        # 2.find the right child node till the end
        # 3.remember reset self node so that we can use it to Recursive's work
        tree = self
        if tree:
            while tree.right:
                tree = tree.right
        return tree

    # x means the node root value
    def insert(self, x):
        if x < self.key:
            # 1.insert left till the tree's end
            if self.left:
                # 2.if left is not None, then do Recursive's work
                self.left.insert(x)
            else:
                # 3.if left is None
                # 4.create a node based on root(x)
                # 5.then finished the insert process
                tree = BinarySearchTree(x)
                self.left = tree
        elif x > self.key:
            # 1.insert right till the tree's end
            if self.right:
                self.right.insert(x)
            else:
                tree = BinarySearchTree(x)
                self.right = tree

    def delete(self, x):
        # 1.firstly: find the node
        if self.find(x):
            # 2.if x is smaller than root, then delete left
            # 3.after delete, we need to reset node
            # 4.self.left = self.left.delete(x)
            # 5.so we can use it to Recursive till the end
            if x < self.key:
                self.left = self.left.delete(x)
                return self
            # 6.x is bigger than root, do the same work
            elif x > self.key:
                self.right = self.right.delete(x)
                return self
            # 7.when x == self.key and the node has left and right child
            elif self.left and self.right:
                # 1.find min Node through right node, and get the min value
                # 2.reset current node key value
                # 3.delete old node key value
                key = self.right.findMin().key
                self.key = key
                self.right = self.right.delete(key)
                return self
            # 8. when x == self.key and the node has no child or one only
            else:
                if self.left:
                    return self.left
                else:
                    return self.right
        # None: can't find
        else:
            return self
