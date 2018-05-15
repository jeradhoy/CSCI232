"""
CSCI232 Program 1
Author: Jerad Hoy
Date: 05/15/2018
Description: This program creates a binary search tree with
"""
class Node(object):
    """Node class for tree"""
    # children of nodes needs to be null

    def __init__(self, data, leftChild, rightChild):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild


class Tree(object):
    """Tree for binary search tree"""

    def __init__(self, root):
        self.root = root

    def find(self, data):
        """Method to search tree for a node, and return true if found"""

    def insert(self, data):
        """Method to inseta a node into the tree, and return true if found"""

    def delete(self, data):
        """Method to delete a node, rebalancing tree."""

        # If nodes children are null, just set parent's child to null
        # If node has one child, just point parent to node's childe
        # If node has two children, find in-order-successor (go right, then all the way left)
        # and swap with node

    def printTree(self):
        """Method to print tree to screen in a human readable way"""

def preOrder(myNode):
    if myNode is None:
        return
    print(myNode.data)
    preOrder(myNode.leftChild)
    preOrder(myNode.rightChild)

def postOrder(myNode):
    if myNode is None:
        return
    preOrder(myNode.leftChild)
    preOrder(myNode.rightChild)
    print(myNode.data)

def inOrder(myNode):

    if myNode == None:
        return
    inOrder(myNode.leftChild)
    print(myNode.data)
    inOrder(myNode.data)

def main():
    # Build and build tree from a comma seperated file called input.txt


if __name__ == '__main__':
    main()