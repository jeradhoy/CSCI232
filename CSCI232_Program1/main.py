"""
CSCI232 Program 1
Author: Jerad Hoy
Date: 05/15/2018
Description: This program creates a binary search tree with inputs either from the user or from an input.txt file. When
run, a tkinter application opens and the user is given the option of loading inputs from file, inserting, deleting, or
finding a node in the tree, which need to be integer inputs. The user can also enter these integers in comma seperated
format to insert. A tree is drawn in the GUI window each time the user makes a change. With find, the node to be found is
highlighted in red if found, and an output is shown on the command line. Likewise, the user can select to traverse the
tree via InOrder, PreOrder, and PostOrder traversal, and the order of this traversal will be printed to the command line.
Tkinter needs to be installed in order to run this app. User needs to enter an integer input into the input box and in
the input.txt file, or application will throw error.
"""

from TreeGUI import *

def main():

    # Builds empty tree and initializes tkinkter session
    TreeGUI(tree=Tree(), root = Tk()).run()

if __name__ == '__main__':
    main()
