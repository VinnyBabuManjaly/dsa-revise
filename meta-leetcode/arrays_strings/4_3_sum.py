"""
3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105

Brute force: 3 nested loops to find three pairs with O(n^3) time complexity
Optimal: Sort and Two pointers with a number fixed
Keep one number i looping from 0 to end
Left pointer at beginning next to i
Right pointer at the end of the array
Result = [] for storings triplet lists with sum 0

While left<right(never equal, since it will consider same number twice)
(Also we are going to check if consecutive numbers are same in the loop 
and ignore those for left and right pointers)
total = nums[i] + nums[left] + nums[right]
if total = 0, result.append([nums[i]], nums[left], nums[right])
    left += 1
    right += 1
    if nums[left] == nums[left+1]: left += 1
    if nums[right] == nums[right-1]: right -= 1
elif total < 0: left += 1
elif total > 0: right -= 1
Return response

Simulation with example:
                     0  1  2 3 4 5
[-1,0,1,2,-1,-4]    -4,-1,-1,0,1,2
result: [[-1,-1,2],[-1,0,1]]

i:nums[i]   left:nums[left] right:nums[right]   total   left<right  result
0:-1        1:-1            5:2                  0      T           [-1,-1,2]
0:-1        3

Time complexity: O(n^2) (Sorting O(nlogn) < rest O(n^2))
Space complexity: O(1)

"""

def three_sum(nums: list) -> list:
    result = []
    nums = sorted(nums)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]: continue
        left, right = i+1, len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0: 
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]: left += 1
                while left < right and nums[right] == nums[right+1]: right -= 1
            elif total < 0: left += 1
            elif total > 0: right -= 1
    return result

if __name__ == "__main__":
    result = three_sum([-1,0,1,2,-1,-4])
    print(result)
