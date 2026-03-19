"""
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
from typing import List
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    bucket = [[] for _ in range(len(nums) + 1)]
    result = [] * k
    
    nums_counter = Counter(nums)
    for num, count in nums_counter.items():
        bucket[count].append(num)
        
    for i in range(len(bucket)-1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result 
        
    
    