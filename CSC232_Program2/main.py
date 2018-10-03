"""
CSCI232 Program 2
Author: Jerad Hoy
Date: 05/22/2018
Description: This program implements a Huffman tree to encode and compress some text, supplied via an input file or the
input dialog box, into binary. This process is displayed via a tkinter app, where the user can load a file, run the
Huffman coding on the text, and see the frequency table, code table, encoded binary, and decoded text. All of this
information is also output to the command line as well.
"""

from HuffmanGUI import *

def main():

    # Start and run the GUI, with a TK master instance
    HuffmanGUI(Tk()).run()

if __name__ == '__main__':
    main()