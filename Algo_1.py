# Palindrome ALGO
# Given an integer x, return true if x is a palindrome, and false otherwise.

"""
Pseudo Code
1.turn input to a string
2.write a for loop to go through string 
3.write a separe variable for a revser string 
4. write a forloop the itirates thru the last value to the begining value to get
reverse value
5. compare original string to reverse string and get value.
6. if reverse  == original it is a palindrome
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_num = ""
        for num in range(len(str(x))-1,-1,-1):
            reverse_num  += str(x)[num]
        print(reverse_num)
        if reverse_num == str(x):
            return True
        else:
            return False