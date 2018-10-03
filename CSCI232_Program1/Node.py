"""
CSCI232 Program 1
Author: Jerad Hoy
Date: 05/15/2018
Description: This class implements a node class for use in the binary search tree.
"""

class Node(object):
    """Node class for storing the node data for leaves in the tree"""
    # children of nodes needs to be null

    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None