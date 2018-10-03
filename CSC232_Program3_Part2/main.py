"""
CSCI 232 Program 3 Part 2
Author: Jerad Hoy
Date: 6/1/2018
Description: This program implements a greedy change making algorithm and tests it
using the unittest package and a testing class.
"""

import unittest

class TestMakeChange(unittest.TestCase):
    """Class to test several cases of the MakeChange greedy algorithm"""

    def test1(self):
        """Test a US coin system with simple case"""
        self.assertEqual(MakeChange([25, 10, 5, 1], 42).makeChange(), [25, 10, 5, 1, 1])

    def test2(self):
        """Test a different coin system with fifty cent piece"""
        self.assertEqual(MakeChange([50, 25, 10, 5, 1], 98).makeChange(), [50, 25, 10, 10, 1, 1, 1])

    def test3(self):
        """Test another basic american coin system"""
        self.assertEqual(MakeChange([25, 10, 5, 1], 79).makeChange(), [25, 25, 25, 1, 1, 1, 1])

    def testEmpty(self):
        """Test that an exception is thrown when we try to create an instance of MakeChange
        with an empty coin system"""
        with self.assertRaises(Exception):
            MakeChange([], 28).makeChange()


class MakeChange:
    """Class to implement a greedy change making algorithm"""

    def __init__(self, coinSystem, amount):
        """Inits coin system and amount to make change for, throws exception if coin system is empty"""
        self.amount = amount

        # If coin system array is empty, throw exception
        if len(coinSystem) > 0:
            self.coinSystem = sorted(coinSystem, reverse=True) # Sort coin system
        else:
            raise Exception("Empty coin array!")

    def makeChange(self):
        """Method to greedily make change for amount, adding each coin to list to return"""

        amount = self.amount
        coins = self.coinSystem
        changeArray = []

        while(amount > 0):

                # Take highest coin, if amount is greater, add coin to changeArray and
                # subtract from amount
                currentCoin = coins[0]
                if amount >= currentCoin:
                    changeArray.append(currentCoin)
                    amount -= currentCoin
                else:
                    coins.pop(0) # If not, discard highest coin and iterate

        return changeArray

if __name__ == "__main__":
    unittest.main() # Run unit tests, no main function needed

