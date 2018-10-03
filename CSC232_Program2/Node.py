"""
CSCI232 Program 2
Author: Jerad Hoy
Date: 05/22/2018
Description: This class implements a node for use in the huffman coding tree. Additionally, it has a method to allow it
to work with a python min heap.
"""

class Node:
    """Class to implement a Node for use in building the Huffman tree"""

    def __init__(self, value=None, char=None, rightChild=None, leftChild=None):
        self.value = value
        self.char = char
        self.rightChild = rightChild
        self.leftChild = leftChild

    def __lt__(self, obj):
        """Method to compare one node to another. Needed for minheap to work"""
        return self.value < obj.value