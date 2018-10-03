"""
CSCI 232 Program 4
Author: Jerad Hoy
Date: 6/04/2018
Description: This program implements Prim's algorithm for finding the minimum spanning tree from any vertex
in a weighted graph. The tree must be provided in an "inputMatrix.txt" file that specifies the adjacency
matrix, where "inf" is used to indicate no connection between nodes. This program will output, to a file
called "output.txt", the list of nodes visited in the order they were visited, and the edges that are included
in the MST found.
"""

import random
import heapq

class Prims:
    """Class to implement Prim's algorithm for finding the MST of a weighted graph"""

    def __init__(self, adjacencyFileName):
        """Constructor to initialize the variables needed for the graph and Prim's"""

        self.adjacencyFileName = adjacencyFileName
        self.adjMatrix = self.__readFromFile__(adjacencyFileName) # Read adjacency matrix from file
        self.nNodes = len(self.adjMatrix)


    def __readFromFile__(self, fileName):
        """Class to read the adjacency matrix from a text file"""

        f = open(fileName, "r")
        contents = f.read()

        # Split the lines on newline character, the numbers on spaces, and convert to floats
        adjMatrix = [[float(x) for x in line.split()] for line in contents.splitlines()]

        f.close()
        return adjMatrix

    def findMST(self, currentNode = None, fileOutput = None):

        # If no node is specified to start, select random node
        if currentNode is None:
            currentNode = random.randint(0, self.nNodes-1)

        visited = [] # Stores which nodes are visited
        edgeVisited = [] # Storing which edges are added to MST
        edgeHeap = [] # Priority queue for Prim's algorithm

        # Loop until we've visited every node
        while True:

            visited.append(currentNode)
            if len(visited) == self.nNodes:
                break

            # Pull out adjacency row from matrix
            adjVertexs = self.adjMatrix[currentNode]

            i = 0
            for edge in adjVertexs:
                if edge != float("inf"):
                    if i not in visited:

                        # If node is connected and we haven't visited it, push to heap
                        heapq.heappush(edgeHeap, (edge, (currentNode, i)))
                i += 1

            # Pop the top edge off the heap, add to edgeVisited, and go to node
            newNodeTuple = heapq.heappop(edgeHeap)
            edgeVisited.append(newNodeTuple[1])
            currentNode = newNodeTuple[1][1]

        # If a file output is specified, output to file, otherwise return the visited list
        if fileOutput is not None:

            f = open(fileOutput, "w+")
            f.write("Visited = " + str(visited) + "\n") # write node visited list to file

            # Write the edge visited list to the file so we know what edges are in MST
            f.write("Edges in MST:\n")
            for edge in edgeVisited:
                f.write(str(edge) + "\n")
            f.close()
            return
        else:
            return visited


def main():

    # Initialize Prims instance, and find the MST starting at node 0, outputing to text file
    myPrim = Prims("inputMatrix.txt")
    myPrim.findMST(0, "output.txt")


if __name__ == "__main__":
    main()
