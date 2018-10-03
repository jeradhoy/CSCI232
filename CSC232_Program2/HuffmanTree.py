"""
CSCI232 Program 2
Author: Jerad Hoy
Date: 05/22/2018
Description: This class implements a Huffman tree to encode a message provided when an instance of the class is created.
It builds a frequency table, generates the huffman tree, builds a code table, encodes the message, and provides methods
for printing these.
"""

from Node import *
from heapq import heappush, heappop

class HuffmanTree:
    """Class to implement a huffman tree to encode and decode a message via huffman coding."""

    def __init__(self, string):
        self.string = string
        self.root = None
        self.codeDict = {}

        # Build the frequency table, huffman tree, and generate codes
        self.freqTable = self.generateFreqTable(string)
        self.build()
        self.generateCodes()

    def generateFreqTable(self, myString):
        """Method to generate a freqency table (here ordered list) for characters"""

        # First use a dictionary for easy access
        freqDict = {}

        # Iterate over letters in the string, counting letters for freqency
        for letter in myString:
            if letter in freqDict.keys():
                freqDict[letter] += 1
            else:
                freqDict[letter] = 1

        # Convert the frequency dictionary to a sorted list of tuples
        freqTable = sorted(freqDict.items(), key=lambda x: x[1])

        return(freqTable)

    def build(self):
        """Method to build a huffman tree after frequency table has been generated."""

        nodeHeap = []

        # Iterate through freqency table and create a node from each character
        for character in self.freqTable:
            heappush(nodeHeap, Node(character[1], character[0]))

        # Iterate through the heap, connecting smallest frequency nodes to build graph
        while len(nodeHeap) > 1:
            left = heappop(nodeHeap) # Pop off the smallest frequency node
            right = heappop(nodeHeap)
            newNode = Node(value=left.value + right.value)
            newNode.leftChild = left
            newNode.rightChild = right
            heappush(nodeHeap, newNode) # Push new node back onto the heap

        # Once all nodes have been joined set this single node (root of huffman tree) to root
        self.root = heappop(nodeHeap)

    def generateCodes(self, myNode = None, code = ''):
        """Recursive method to generate codes for each character in Huffman tree"""

        # Initial case, set myNode to root
        if myNode is None:
            myNode = self.root

        # Base case, if we are at a character node, insert code into codeDict
        if myNode.char is not None:
            self.codeDict[myNode.char] = code
        else:
            self.generateCodes(myNode.leftChild, code + '0') # Go left
            self.generateCodes(myNode.rightChild, code + '1') # Go right

    def printFreqTable(self):
        """Method to return a string containing a formatted frequency table."""

        table = ""
        for character in self.freqTable:
            table += str(character[0]).replace("\n", "\\n").ljust(2) + "|" + str(character[1]) + "\n"
        return table

    def printCodeTable(self):
        """Method to return a string containing a formatted code table."""

        table = ""
        for character in self.freqTable:
            table += character[0].replace("\n", "\\n").ljust(2) + "|" + self.codeDict[character[0]] + "\n"
        return table

    def encode(self):
        """Method to encode the given string into a binary string using the code table."""

        encodedString = ''

        # Iterate over string, appending code to the output string
        for character in self.string:
            encodedString += self.codeDict[character]

        return encodedString

    def decode(self):
        """Method to take an encoded binary string and decode it by traversing the huffman tree."""

        encodedString = self.encode()
        decodedString = ''

        currentNode = self.root

        # iterate over encoded binary string, traverse if not at a leaf node, and return character if at leaf node
        for digit in encodedString:

            if digit == '0':
                currentNode = currentNode.leftChild
            else:
                currentNode = currentNode.rightChild

            # If we are at a leaf node, append character to output string, and go back to the root
            if currentNode.char is not None:
                decodedString += currentNode.char
                currentNode = self.root

        return decodedString
