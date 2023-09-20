# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 


"""
What are we doing?
returning an index with the value equal to target var.

If the  value is not in the array  return the index  where it can  be inserted in order.

example 1
nums = [1,4,7,8,9] target = 3
output = 1

nums = [0,2,4,5,7] target = 2
output = 1


target_in_array = False

for index in nums
    if nums[index] == target
        print index
        target_in_array = True

if target_in_array == False
    for index in nums
    #if the nums[index] value  is - 1 from target take the index +1 after it
        if nums[index] == target - 1
            print[index + 1]

"""
# nums = [1,3,5,6], target = 5

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        target_in_array = False

        # for index, value in enumerate(nums):
        #     if value == target:
        #         index_val = index
        #         print(index_val)
        #         target_in_array = True
        #         return

        # if target_in_array == False:
        #     for index, value in enumerate(nums):
        #     #if the nums[index] value  is - 1 from target take the index +1 after it
        #         if value == target - 1:
        #             index_val = index +1
        #             print(index_val)
        #             return

        for index, value in enumerate(nums):
            if value >= target:
                return index
        return len(nums)