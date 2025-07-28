"""
Sliding Window Median
Hard
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.
For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]

Constraints:
1 <= k <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""

def moving_median(nums: list, k: int) -> list:
    """
    Sliding window base
    window_start = 0
    window_sum = 0
    max_sum = 0
    
    for window_end in range(len(nums)):
        window_sum += nums[window_end]
    window_start = 0
        if window_end - window_sum + 1 == k:    
            max_sum = max(max_sum, window_sum)
            window_sum -= window_sum[window_start]
            window_start += 1
    return max_sum
    """
    window_start, window_sum, window_avg = 0, 0, 0.0
    result = []
    
    for window_end in range(len(nums)):
        window_sum += float(nums[window_end])
        if window_end - window_start + 1 == k:
            result.append(window_sum / k) 
            window_sum -= nums[window_start]
            window_start += 1
    return result
           
        
"""       
 0 1  2  3 4 5 6 7
[1,3,-1,-3,5,3,6,7]         k=3
start   end nstart  nend  sum avg     sum
0       0   1       1       1   -       -
0       1   1       3       4   -       -
0       2   1       -1      3   1       0
1       3   3       -3      -3           
           

"""       