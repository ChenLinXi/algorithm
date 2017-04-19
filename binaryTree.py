#coding=utf-8

class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self):
        self.root = Node()

    '''add node'''
    def add(self, elem):
        node = Node(elem)
        '''check root'''
        if self.root.elem == -1:
            self.root = node
        else:
            myQueue = []    # list pop(0)
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:
                treeNode = myQueue.pop(0)
                if treeNode.lchild == None:
                    treeNode.lchild = node
                    return
                elif treeNode.rchild == None:
                    treeNode.rchild = node
                    return
                else:
                    myQueue.append(treeNode.lchild)
                    myQueue.append(treeNode.rchild)

    def front_digui(self, root):
        '''root left right'''
        if root == None:
            return
        print root.elem
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):
        '''left root right'''
        if root == None:
            return
        self.middle_digui(root.lchild)
        print root.elem
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        '''left right root'''
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print root.elem

    def front_stack(self, root):
        '''root left right'''
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:     #begin with root node, find its left child till end
                print node.elem
                myStack.append(node)
                node = node.lchild
            node = myStack.pop() # list pop the last node
            node = node.rchild   # find its right node

    def middle_stack(self, root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:     # find its left child node
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()    # when left finished, print root and find its right again
            print node.elem # print root element
            node = node.rchild # find its right child node

    def later_stack(self, root):
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:
            node = myStack1.pop()   # find its left child and right child
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)   # store node info to the other list
        while myStack2: # print root element
            print myStack2.pop().elem

    def level_queue(self, root):
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)   # list pop till Queue is empty
            print node.elem # print root element
            if node.lchild != None:
                myQueue.append(node.lchild) # find its left child root
            if node.rchild != None:
                myQueue.append(node.rchild) # find its right child root

if __name__ == "__main__":
    elems = range(10)
    tree = Tree()
    for elem in elems:
        tree.add(elem)

    print '队列实现层次遍历:'
    tree.level_queue(tree.root)

    # print '\n\n递归实现先序遍历:'
    # tree.front_digui(tree.root)
    # print '\n递归实现中序遍历:'
    # tree.middle_digui(tree.root)
    # print '\n递归实现后序遍历:'
    # tree.later_digui(tree.root)
    #
    # print '\n\n堆栈实现先序遍历:'
    # tree.front_stack(tree.root)
    # print '\n堆栈实现中序遍历:'
    # tree.middle_stack(tree.root)
    # print '\n堆栈实现后序遍历:'
    # tree.later_stack(tree.root)
