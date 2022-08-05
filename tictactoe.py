"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #20 - Tic Tac Toe (tictactoe.py)


Author: Carter Berlind

Difficulty Level: 9/10

Prompt: Alexander challenges you to a game of Tic Tac Toe. Knowing the success of computers 
in games such as chess and go, you decide to give computers the much more challenging task of 
playing Tic Tac Toe. Your task is to create a function that, when given two positions on a 
Tic Tac Toe board, finds a square that completes it. If there is no square, return that 0. 
Inputs should be 2 integers from 1-9 representing position as shown below.

1   2   3
4   5   6
7   8   9

The output should be an integer representing a position on the board.

Constraints: If input integers are outside of this range, return the string “invalid”

Test Cases:
Input: 1,5;     Output: 9
Input: 2,3;     Output: 1
Input: 6,8;     Output: 0
Input: 7,3;     Output: 5
Input: 1,7;     Output: 4
"""

class Solution:
    def tic_tac_toe(self,a,b):
        # type a: int
        # type b: int
        # return type: int

        # TODO: Write code below to return an int with the solution to the prompt
        if a == 1 and b == 2 or a == 2 and b == 1:
            return 3
        elif a == 2 and b == 3 or a == 3 and b == 2:
            return 1
        elif a == 1 and b == 3 or a == 3 and b == 1:
            return 2

        elif a == 4 and b == 5 or a == 5 and b == 4:
            return 6
        elif a == 6 and b == 5 or a == 5 and b == 6:
            return 4
        elif a == 6 and b == 4 or a == 4 and b == 6:
            return 5

        elif a == 7 and b == 8 or a == 8 and b == 7:
            return 9
        elif a == 9 and b == 8 or a == 8 and b == 9:
            return 7
        elif a == 9 and b == 7 or a == 7 and b == 9:
            return 8

        elif a == 7 and b == 1 or a == 1 and b == 7:
            return 4
        elif a == 7 and b == 4 or a == 4 and b == 7:
            return 1
        elif a == 1 and b == 4 or a == 4 and b == 1:
            return 7

        elif a == 2 and b == 8 or a == 8 and b == 2:
            return 5
        elif a == 5 and b == 8 or a == 8 and b == 5:
            return 2
        elif a == 5 and b == 2 or a == 2 and b == 5:
            return 8

        elif a == 3 and b == 9 or a == 9 and b == 3:
            return 6
        elif a == 6 and b == 9 or a == 9 and b == 6:
            return 3
        elif a == 6 and b == 3 or a == 3 and b == 6:
            return 9

        elif a == 7 and b == 3 or a == 3 and b == 7:
            return 5
        elif a == 5 and b == 3 or a == 3 and b == 5:
            return 7
        elif a == 5 and b == 7 or a == 7 and b == 5:
            return 3

        elif a == 1 and b == 9 or a == 9 and b == 1:
            return 5
        elif a == 5 and b == 9 or a == 9 and b == 5:
            return 1
        elif a == 5 and b == 1 or a == 1 and b == 5:
            return 9

        else:
            return 0

def main():
    num1 = int(input())
    num2 = int(input())

    tc1 = Solution()
    ans = tc1.tic_tac_toe(num1,num2)
    print(ans)

if __name__ == "__main__":
    main()