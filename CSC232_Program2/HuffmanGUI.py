"""
CSCI232 Program 2
Author: Jerad Hoy
Date: 05/22/2018
Description: This class implements a tkinter GUI for reading in a message, encoding it with a huffman tree, and
displaying the results.
"""

from HuffmanTree import *
from tkinter import *
from tkinter.filedialog import askopenfile

class HuffmanGUI:
    """Class to create a tkinter application for creating a Huffman tree and encoding a given message."""

    def __init__(self, root, tree=None, height = 400, width = 400):
        """Constructor method for initializing the tree application"""

        self.tree = tree
        self.root = root

        self.loadButton = Button(self.root, text = "Load From File", command = self.loadFromFile)
        self.loadButton.grid(row=0, columnspan=4)

        self.textEnter = Text(self.root, height = 8, font = "courier")
        self.textEnter.grid(row = 1, columnspan=4)

        self.runButton = Button(self.root, text = "Run", command = self.runHuffman)
        self.runButton.grid(row = 2, columnspan = 4)

        self.freqLabel = Label(self.root, text = "Frequency Table:")
        self.freqLabel.grid(row = 3, column = 0)

        self.freqText = StringVar()
        self.freqTable = Message(self.root, textvariable = self.freqText, font = "courier")
        self.freqTable.grid(row=4, column=0)

        self.codeLabel = Label(self.root, text = "Code Table:")
        self.codeLabel.grid(row = 3, column = 1)

        self.codeText = StringVar()
        self.codeTable = Message(self.root, textvariable = self.codeText, font = "courier")
        self.codeTable.grid(row=4, column=1)

        self.binaryLabel = Label(self.root, text = "Encoded Binary:")
        self.binaryLabel.grid(row = 3, column = 2)

        self.textVar = StringVar()
        self.binaryOutput = Message(self.root, textvariable = self.textVar, font = "courier")
        self.binaryOutput.grid(row=4, column=2)

        self.decodedLabel = Label(self.root, text = "Decoded Text:")
        self.decodedLabel.grid(row = 3, column=3)

        self.textVar2 = StringVar()
        self.decodedOutput= Message(self.root, textvariable = self.textVar2, font = "courier")
        self.decodedOutput.grid(row=4, column=3)

    def loadFromFile(self):
        """Method to browse for and open a text file containing the message that we want to encode."""

        file = askopenfile()
        self.textEnter.insert(INSERT, file.read())

    def runHuffman(self):
        """Method to create a huffman tree and encode the provided message, displaying the frequency table and code table
        as well"""

        # Read message from text box and print to console
        text = self.textEnter.get("1.0","end-1c")
        print("\nOriginal Message:\n", repr(text), sep="")

        # Build a huffman tree from the text
        self.tree = HuffmanTree(text)

        # Generate our frequency and code tables
        freqTable = self.tree.printFreqTable()
        codeTable = self.tree.printCodeTable()

        # Print the tables to the command line
        print("\nFrequency Table:\n", freqTable, sep="")
        print("\nCode Table:\n", codeTable, sep="")

        # Display the tables in the app
        self.freqText.set(freqTable)
        self.codeText.set(codeTable)

        # Encode the message and print it to the command line and the GUI
        encodedText = self.tree.encode()
        print("Encoded Message:\n", encodedText, sep="")

        # Decode the message and print it to the command line and GUI
        decodedText = self.tree.decode()
        open("output.txt", "w").write(decodedText)

        # Display the enocded and decoded messages in the GUI
        self.textVar.set(encodedText)
        self.textVar2.set(decodedText)

    def run(self):
        """Method to start the main evaluation loop for the tkinter object"""

        self.root.mainloop()
