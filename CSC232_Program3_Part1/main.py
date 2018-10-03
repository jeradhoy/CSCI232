"""
CSCI 232 Program 3 Part 1
Author: Jerad Hoy
Date: 6/1/2018
Description: This program implements a hash table with open addressing and quadratic probing.
Additionally, it provides a command line interface for interacting with the hash table
"""

class Menu:
    """Class to implement a menu for interacting with the hash table"""

    def __init__(self, table):
        """Init method for initializing the menu, taking a hash table as input."""
        self.table = table

    def run(self):

        # Infinitely loop, taking inputs from command line until prompted to exit
        while(True):

            # Display menu to user
            print("\nEnter x to quit:")
            print("Enter p to print the hash table:")
            print("Enter i to insert into the hash table:")
            print("Enter s to search for a value in the hash table:")
            print("Enter d to delete a value in the hash table:")

            answer = input()

            # Take action depeding on input
            if(answer == "i"):
                val = input("Enter the value to input: ")
                self.table.insert(int(val))
            elif(answer == "p"):
                self.table.printTable()
            elif(answer == "s"):
                val = input("Enter the value to search for: ")
                self.table.search(int(val))
            elif(answer == "d"):
                val = input("Enter the value to delete: ")
                self.table.delete(int(val))
            elif(answer == "x"):
                print("Goodbye!")
                return


class KeyValPair:
    """Class to create a key-value pair for items in the hash table."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        """Method to override the print method to return formatted key-value string."""
        return(str(self.key).rjust(3) + " | " + str(self.value))

class HashTable:
    """Class to implement a hash table, here an array of KeyValPair objects"""

    def __init__(self, size = 8):
        """Method to initialize the hash table to a default size of 8 and an array of None values."""
        self.size = size
        self.array = [None] * size

    def insert(self, val):
        """Method to insert a value into the hash table with quadratic probing"""

        i = 0

        # Iterate with quadratic probing until space is found
        while(True):

            key = val % self.size + i**2

            # If no key-val pair is in array, put it in
            if self.array[key] is None:
                self.array[key] = KeyValPair(key, val)
                break
            i += 1

        # After insertion, check balance factor and rebalance if neccessary
        self.rebalanceTable();
        return

    def search(self, val):
        """Method to search for a value in the hash table"""

        i = 0

        # Iterate with quadratic probing until val is found
        while(True):
            key = val % self.size + i**2

            if self.array[key].value == val:
                print("Value " + str(val) + " found at index " + str(key))
                return
            i += 1

        print("Value " + str(val) + " not found.")

    def delete(self, val):
        """Method to find and delete a value in the hash table."""

        i = 0

        # Iterate with quadratic probing until val is found
        while(True):
            key = val % self.size + i**2

            if self.array[key].value == val:

                self.array[key] = None # Set space to None if found
                print("Value " + str(val) + " deleted.")
                return
            i += 1

        print("Value " + str(val) + " not found.")
        return

    def doubleSize(self):
        """Method to double size of array when load factor >= 0.8"""

        # Store old array for rehashing
        oldArray = self.array

        # Double array size and create new hash table array
        self.size = self.size * 2
        self.array = [None] * self.size

        # Rehash all values in old array
        for keyVal in oldArray:
            if keyVal is not None:
                self.insert(keyVal.value)

    def rebalanceTable(self):
        """Method to check the load factor of the hash table, double size, and rehash."""

        loadFactor = sum(x is not None for x in self.array)/self.size

        if loadFactor >= 0.8:
            print("Rebalancing Array")
            self.doubleSize()
        return

    def printTable(self):
        """Method to print out the contents of the hash table"""

        print("Key | Value")
        print("-----------")
        for keyVal in self.array:
            print(keyVal)
        print()
        return



def main():

    myHash = HashTable()
    Menu(myHash).run()

if __name__ == '__main__':
    main()
