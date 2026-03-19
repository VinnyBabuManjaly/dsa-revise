"""Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

nums = [-2,1,-3,4,-1,2,1,-5,4]    

Brute force solution: Calculating largest sum and keeping track of the maximum value with each element being the first element in the sub array

Optimal solution: Kadane's algorithm
Tracking only the maximum count, not the actual subarray is to be taken into output

- Traverse through each element in the group
    - Keep a current sum variable, while traversing recaluclate the current sum by adding each element
        - When each element comes current sum in max(current element, current sum + element)
        - Which means we decide like whether we should take the new sub array or extend the existing one
    - Keep a global sum or largest sum variable as max(largest sum, current sum) based on the new current sum
- REturn largest sum itself

Time complexity - O(n) - Single pass
Space complexity - O(1) - Only constant number of additional variables
"""

class MaximumSubarraySolver:
    def maximum_subarray(self, nums: list[int]) -> int:
        current = largest = nums[0]
        for num in nums[1:]:
            current = max(current + num, num)
            largest = max(current, largest)
        return largest
    

if __name__ == "__main__":
    solver = MaximumSubarraySolver()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = solver.maximum_subarray(nums)
    print(result)