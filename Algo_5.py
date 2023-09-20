"""# temp_val = 10
# string_val = str(temp_val)
# string_val_one = string_val[0]
# print(string_val_one)
# string_val_two = string_val[1]
# print(string_val_two)   

# integer_value = 10
# string_with_comma = str(integer_value)[0] + ',' + str(integer_value)[1]
# print(string_with_comma)

# digits = [1,2,3,9]

# len(digits - 1) = len(digits - 1) + 1
# if len(digits - 1)  > 9
#     temp_val = len(digits - 1)
#     string_val = str(temp_val )
#     int_val_one = int(temp_val[0])
#     int_val_two = int(temp_val[1])
#     digits.pop(len(digits - 1))
#     digits.insert(int_val_one,int_val_two)
#     print(digits)
#     return digits
"""

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

#Answer 


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)
        
        # Start from the rightmost digit
        carry = 1  # Initialize carry to 1 for adding 1
        for i in range(n - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        
        # If there's still a carry, insert it at the beginning
        if carry > 0:
            digits.insert(0, carry)
        
        return digits