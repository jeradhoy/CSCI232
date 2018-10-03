"""
CSCI232 Program 1
Author: Jerad Hoy
Date: 05/15/2018
Description: This class creates a tree from a root node and allows the user to find, delete, insert, and print
tree traversal orders from the tree.
"""

from Node import *

class Tree(object):
    """Tree class for a binary search tree, with methods for inserting, finding, deleting, and traversing the tree"""

    def __init__(self):
        self.root = None

    def find(self, key):
        """Method to search tree for a node, and return true if node is found"""

        # If the root is None, then we are done and node is not in tree
        if self.root is None:
            return False
        else:

            current = self.root

            #  Loop through tree, traversing left or right depending on node value
            while True:
                if current is None: # Exit if we have reached the end of the tree
                    return False
                elif key == current.key:
                    return True
                elif key < current.key: # go left
                    current = current.leftChild
                else: # go right
                    current = current.rightChild

    def delete(self, key):
        """Method to delete a node, repointing child nodes to proper parent."""

        # If tree is empty, exit now, as there is no node to delete
        if self.root is None:
            return False

        current = self.root
        parent = current
        isLeftChild = False

        # loop through tree, find node that matches key in similar method to find, above
        while True:
            if current is None:
                return False
            elif key == current.key:
                break
            elif key < current.key: # go left
                parent = current
                isLeftChild = True
                current = current.leftChild
            else: # go right
                parent = current
                isLeftChild = False
                current = current.rightChild

        # Case 1: If nodes children are null, just set parent's child to null
        if current.rightChild is None and current.leftChild is None:
            if current == self.root:
                self.root = None
            elif isLeftChild:
                parent.leftChild = None
            else:
                parent.rightChild = None

        # Case 2: If node has one child, just point parent to node's child
        elif current.rightChild is None: # point left child to parent
            if current == self.root:
                self.root == current.leftChild
            elif(isLeftChild):
                parent.leftChild = current.leftChild
            else:
                parent.rightChild = current.leftChild
        elif current.leftChild is None:
            if current == self.root:
                self.root == current.rightChild
            elif(isLeftChild):
                parent.leftChild = current.rightChild
            else:
                parent.rightChild = current.rightChild

        # If node has two children, find in-order-successor (go right, then all the way left)
        else:
            inOrderSuccessor = current.rightChild
            parent = current
            isLeftChild = False

            # Loop through tree, going right once, then all the way left
            while True:

                if inOrderSuccessor.leftChild is None:
                    break
                else:
                    isLeftChild = True
                    parent = inOrderSuccessor
                    inOrderSuccessor = inOrderSuccessor.leftChild

            if isLeftChild:
                parent.leftChild = inOrderSuccessor.rightChild
            else:
                parent.rightChild = inOrderSuccessor.rightChild

            # Replace node to be deleted with in order successor
            current.key = inOrderSuccessor.key

    def insert(self, key):
        """Method to insert a node into the tree"""

        newNode = Node(key)

        # If root is none, just insert newNode into root
        if self.root is None:
            self.root = newNode
            return
        else:
            current = self.root

            # Loop through tree, going left or right and inserting it when we can
            while True:
                parent = current

                # Screen for duplicate keys
                if key == current.key:
                    print("\nError: Duplicate key!")
                    return
                elif key < current.key: # go left
                    current = current.leftChild
                    if current is None:
                        parent.leftChild = newNode
                        return
                else:
                    current = current.rightChild
                    if current is None:
                        parent.rightChild = newNode
                        return

    def preOrder(self, myNode=0):
        """Method to print the preOrder traversal to the console"""

        if myNode == 0:
            myNode = self.root

        if myNode is None:
            return
        print(myNode.key)
        self.preOrder(myNode.leftChild)
        self.preOrder(myNode.rightChild)

    def postOrder(self, myNode=0):
        """Method to print the postOrder traversal to the console"""

        if myNode == 0:
            myNode = self.root

        if myNode is None:
            return
        self.postOrder(myNode.leftChild)
        self.postOrder(myNode.rightChild)
        print(myNode.key)

    def inOrder(self, myNode=0):
        """Method to print the inOrder traversal to the console"""

        if myNode == 0:
            myNode = self.root

        if myNode is None:
            return
        self.inOrder(myNode.leftChild)
        print(myNode.key)
        self.inOrder(myNode.rightChild)

