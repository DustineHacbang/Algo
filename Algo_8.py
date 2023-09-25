"""

-we are gonna need a variable called longest_prefix variable

-we will return "longest_prefix" var

input = [ladder,lad,large]
output = "la"

input =[apple, acorn, arm, ]
output = "a"

_____________________________________________________________

for loop words in the string list 
    - we want to get the first string and set  to a variable  to compare
    - we want to compare  the first string to all the other string in the list
    - each time it passes through the list it wil subtract a letter to the  varibale containing the first string
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest_prefix = strs[0]

        for words in strs:
            if longest_prefix == words:
                continue 

            while True:
                if longest_prefix == "":
                    break
                if words.startswith(longest_prefix):
                    break
                else:
                    longest_prefix = longest_prefix[:-1]

        return longest_prefix