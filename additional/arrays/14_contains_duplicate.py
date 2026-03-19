"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3
Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:All elements are distinct.
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
ARCHITECT
"""
def contains_duplicate(nums: list) -> bool:
    nums_dict = {}
    
    for i, num in enumerate(nums):
        if nums_dict[num] in nums_dict:
            return False
        nums_dict[num] = i
    return True
        
"""        
Example iteration:
        0 1 2 3
nums = [1,2,3,1]

i   num dict[num]   
0   1   -   dict[1] = 0
1   2   -   dict[2] = 1
2   3   -   dict[3] = 2
3   1   0   

Edge cases:
Single elem


"""