"""Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Brute force solution:
- Take each elements one by one and add it to the other numbers in the array to check for the target.
- Continue for elements until the target sum is possible, since at least on solution exists

Optimal solution: Hashing
- Generate a dictionary or hashmap such that all elements in the input array are keys and their respective indices are the values.
- Calculate the complement = target - element, for each element
- if the complement already exists in dictionary, return index from the value in dictionary and index of the current element
- else add that value to the dictionary

Time complexity - O(n) - Single pass
Space complexity - O(1) - Only constant number of additional variables

"""
from typing import List

class TwoSumSolver:
    def twoSum(self, nums: list, target: list) -> List:
        compDict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in compDict:
                return [i, compDict[complement]]
            compDict[num] = i


if __name__ == "__main__":
    solver = TwoSumSolver()
    nums = [3, 2, 4]
    target = 7
    result = solver.twoSum(nums, target)
    print(result) 

