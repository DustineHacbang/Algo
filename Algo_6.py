# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.



'''
we need to create variables that gives roman nums an integer

we need a for loop that will itirate thru the string 

as its going through the string  the program will read each letter  then give it a value based on the roman numerals

onces it is given a value it will all be combined to gether to give the sum of the input 


# examples

innputs: IV
output: 4

input: XV 
output: 15


# sample code
romen_dic
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

for index , value in  enumerate(s):
    if value 

input  xxiv
output 24
temp = [10,10,-1,5]

input  xvii
output 24
temp = [10,5,1,1]


'''

class Solution:
    def romanToInt(self, s: str) -> int:
        
        total_roman_val = 0

        temp_array = []

        roman_dic = {
            "I":1,
            "V":5,
            "X":10,        
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }        

        for index, value in enumerate(s):
            roman_val_1 = roman_dic[value]
            try:
                one_index_ahead = s[index + 1]
                roman_val_2 = roman_dic[one_index_ahead]
            except:
                temp_array.append(roman_val_1)
                break

            if roman_val_1 < roman_val_2:
                temp_array.append(roman_val_1 * -1 ) 
            
            else:
                temp_array.append(roman_val_1)

        total_roman_val = sum(temp_array) 


        return total_roman_val