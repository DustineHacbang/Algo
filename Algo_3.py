"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""

# nums = [1,3,5,6], target = 5

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        target_in_array = False

        for index in nums:
            if nums[index] == target:
                print(index)
                target_in_array = True

        if target_in_array == False:
            for index in nums:
            #if the nums[index] value  is - 1 from target take the index +1 after it
                if nums[index] == target - 1:
                    print(index + 1)
