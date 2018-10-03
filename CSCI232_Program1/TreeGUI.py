"""
CSCI232 Program 1
Author: Jerad Hoy
Date: 05/15/2018
Description: This class implements a tkinter based GUI for creating the binary search tree, inserting nodes,
loading nodes from a text file, deleting, finding, and traversing tree, as well as drawing the tree at each step.
"""

from tkinter import *
from tkinter.filedialog import askopenfile
from math import exp
from Tree import *

class TreeGUI:
    """Class to create a tkinter application for manipulating and displaying a binary search tree."""

    def __init__(self, tree, root, height = 400, width = 400):
        """Constructor method for initializing the tree application"""
        self.tree = tree
        self.root = root

        self.frame = Frame(self.root, width = width, height = height) # Frame to host all of application
        self.frame.pack(fill = "both", expand = True) # Allows frame to expand to allow for bigger tree

        self.loadButton = Button(self.frame, text = "Load From File", command = self.loadFromFile)
        self.loadButton.pack(side = "top")

        self.entry = Entry(self.frame)
        self.entry.pack(side = "right")

        self.insertButton = Button(self.frame, text = "Insert", command = self.insertToTree)
        self.insertButton.pack(side = "left")

        self.deleteButton = Button(self.frame, text = "Delete", command = self.deleteFromTree)
        self.deleteButton.pack(side = "left")

        self.find = Button(self.frame, text = "Find", command = self.findInTree)
        self.find.pack(side = "left")

        self.traversalOption = StringVar(self.frame)
        self.options = OptionMenu(self.frame, self.traversalOption, *["InOrder", "PreOrder", "PostOrder"],
                                  command = self.traverseTree)
        self.options.pack(side = "left")

        self.canvas = Canvas(self.root)
        self.canvas.pack(fill = "both", expand = True)

    def traverseTree(self, option):
        """Method to print tree traversal order's to command line when dropdown menu is clicked"""

        if option == "InOrder":
            print("\nInOrder Tree Traversal:")
            self.tree.inOrder()

        if option == "PreOrder":
            print("\nPreOrder Tree Traversal:")
            self.tree.preOrder()

        if option == "PostOrder":
            print("\nPostOrder Tree Traversal:")
            self.tree.postOrder()

    def loadFromFile(self):
        """Method to browse for and open a comma seperated text file and insert into tree."""

        file = askopenfile()
        self.parseAndInsert(file.read())
        self.drawTree()

    def parseAndInsert(self, text):
        """Method to parse a comma-seperated string and input the values into the tree."""

        input = [int(x.strip()) for x in text.split(",")] # Split on comma and strip whitespace
        for x in input:
            self.tree.insert(x)
        return

    def insertToTree(self):
        """Method to insert nodes into tree from values in input box. Can be comma-seperated."""

        self.canvas.delete("all")
        self.parseAndInsert(self.entry.get())
        self.drawTree()

    def deleteFromTree(self):
        """Method to delete a node from the tree, given one at a time in the input box. Cannot be comma-seperated."""
        self.canvas.delete("all")
        self.tree.delete(int(self.entry.get()))
        self.drawTree()

    def findInTree(self):
        """Method to find a key in the tree, and redraw with node highlighted, and output message to command line."""

        self.canvas.delete("all")

        number = self.entry.get()
        if number == '':
            print("Please enter an integer")
            return

        number = int(number)
        inTree = self.tree.find(number) # Check if key is in tree, and highligh if so
        if inTree:
            print("\nTrue, the number", number, "is in the tree.")
        else:
            print("\nFalse, the number", number, "is not in the tree.")
        self.drawTree(highlightKey=number)

    def drawTree(self, node = 0, xPos = 0, yPos = 30, depth = 1, highlightKey = None, offsetX = 100, offsetY = 40):
        """Recursive method to draw the tree, with decaying width between leaves, and option to highlight a node."""

        # If on first call of method, set node to root and initialize the x position of the nodes
        if node == 0:
            node = self.tree.root
            xPos = self.canvas.winfo_width() / 2 # Get updated width if resizing

        if node is None:
            return

        rad = 10 # Hard coded node circle radius value

        fillColor = "white"

        # If we are on the node to highlight, set the color to red
        if highlightKey is not None:
            if highlightKey == node.key:
                fillColor = "red"

        # Draw oval and text for the node
        self.canvas.create_oval(xPos-rad, yPos-rad, xPos+rad, yPos+rad, fill=fillColor)
        self.canvas.create_text(xPos, yPos, text=str(node.key))

        # Set an exponential width decay based off depth in the tree
        widthDecay = exp(-.3*depth)

        # Create lines below each node that go to the next node to be drawn
        self.canvas.create_line(xPos, yPos+rad, xPos - offsetX*widthDecay, yPos + offsetY-rad)
        self.canvas.create_line(xPos, yPos+rad, xPos + offsetX*widthDecay, yPos + offsetY-rad)

        # Recursively draw left and right child nodes
        self.drawTree(node.leftChild, xPos - offsetX*widthDecay, yPos + offsetY, depth + 1, highlightKey)
        self.drawTree(node.rightChild, xPos + offsetX*widthDecay, yPos + offsetY, depth + 1, highlightKey)

    def run(self):
        """Method to start the main evaluation loop for the tkinter object"""
        self.root.mainloop()
