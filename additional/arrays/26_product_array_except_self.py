"""
Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

[ 1, 2, 3, 4]
[ 1, 1, 2, 6]
[24,12, 4, 1]
[24,12, 8, 6]
"""

def productExceptSelf(nums: list) -> list:
    n = len(nums)
    output = [1] * n
    
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
        
    suffix = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    
    return output

"""
Edge cases: 

Example iteration:
  0  1  2  3  4
[-1, 1, 0,-3, 3]
[0,0,9,0,0]

i   nums    output[1]   prefix
0   -1      1           -1
1   1       -1          -1
2   0       -1          0
3   -3      0           0
4   3       0           -
                        out[i]  suffix
4   3       0           0       3
3   -3      0           0       -9
2   0       -1          9       0
1   1       -1          0       0      
0   -1      1           0       -



  0  1  2  3
[ 1, 2, 3, 4]
i   nums    output[1]   prefix
0   1       1           1
1   2       1           2
2   3       2           6
3   4       6           -
                        output[i]   suffix 
3   4       6           6           4
2   3       2           8           12
1   2       1           12          24
0   1       1           24          -
"""
    