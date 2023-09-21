#TWO SUMS

"""
we will need to pick the correct values on the array that will equal target.

we can try brute forcing it by itierating thru the array  and trying each combination that will equal target.

example:

nums =[5,4,8,1,10] target = 14
output = [4,1]

nums = [6,8,4,3,1] target = 12
output = [1,2]

Psuedo:

for loop to itierate thru the array
    -create variable index_sum_val
    -store value it in called temp_var1
    
    for loop itierating thru the array
        -store value it in called temp_var2
        -if temp_var2 == temp_va1
            pass
        -if temp_var + temp_var2 == target
            index_sum_val append temp_var1
            index_sum_val append temp_var2



    returning index_sum_val
"""



class Solution(object):
    def twoSum(self, nums, target):
        index_sum_val = []  # Initialize an empty list to store indices or values

        for i in range(len(nums)):
            temp_val1 = nums[i]

            for j in range(i + 1, len(nums)):  # Start the inner loop from the next index
                temp_val2 = nums[j]

                if temp_val2 == temp_val1:
                    pass

                if target == temp_val2 + temp_val1:
                    index_sum_val.append(i)
                    index_sum_val.append(j)
                    return index_sum_val  # Return the result if a pair is found

        return index_sum_val  # Return an empty list if no pair is found