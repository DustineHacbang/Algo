"""
Converting Roman Numbers to integers

Pattern:
If the previews index is smaller then the next index it will become the value  before the actual value

Example 
IX = 9
Iv = 4
XL = 40
XC = 90
CD = 400
CM = 900

We will need  a for loop that  will iterate thru the string

"for value in s "

while it is iterating we need it to identify the value
we can set the values in a dictionary

"roman_num = {
"I" : 1,
"V" : 5,
"X" : 10,
"L" : 50,
"C" : 100,
"D" : 500,
"M" : 1000,
}"

once it is identifid  it will be added to an empty variable

roman_val =

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        s = s
        roman_num = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            }


        roman_val = 0
        prev_value = 0

        for char in s:
            current_value = roman_num[char]

            # If the current numeral is greater than the previous numeral, 
            # it means we should subtract twice the previous value 
            # (because we previously added it)
            if current_value > prev_value:
                roman_val += current_value - 2 * prev_value
            else:
                roman_val += current_value

            prev_value = current_value

        return roman_val

            
        return roman_val