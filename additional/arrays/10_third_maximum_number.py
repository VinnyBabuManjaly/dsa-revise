"""
Third Maximum Number
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 3:
Input: nums = [2,2,3,1,4]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

Brute force: Sorting the distinct elements(set for unique elements) and returning the 3rd value in the array. If 3rd doesn't exist, return the last in the array.

Optimal solution: 
Track top 3 maximas in single pass
- initialize max1, max2, max3 to 0
- traverse through elements until the end
    - check from highest max, ie max1. So,
    - if num>max1, max3=max2, max2=max1, max1=num
    - if num>max2 and num<max1, from max2, i.e max3=max2, max2=num
    - if num>max3 and num<max2, max3= num
- return max3

Similation with example:
 0 1 2 3
[2,2,1,3,1,0,5] Output=2

            out
nums    max3    max2    max1
        -inf    -inf    -inf    initial
        1       2       3       expected
2       -inf    -inf    2       shift left/fill from max1
2       -       -       -       no change 
1       -inf    1       2
3       2       2       3       shift left/fill from max1
1       1       2       3       shift right/fill from max3     
0       -       -       -       no change
5       2       3       5       shift left/fill from max1   

Time complexity: O(n)
Space complexity: O(1)

Edge cases:
[]          None    empty
[1]         1       just one element
[1,2]       2       two elements
[1,2,3]     3       three elements
[1,2,3,4]   2       normal, valid
[1,1,1,1]   1       all same elements
[0,0,0,0]   0       all zeroes
[0,2,3,3,3] 0       multiple third maximum
[1,1,2,2]   2       no third maximum
[1,1,1]     1       no 2nd and 3rd maximums
[1,2,3,4]   2       increasing order
[4,3,2,1]   2       decreasin order
[1,2,3,4,2,1] 2     altogether 
"""

class ThirdMaximumNumberSolver():
    def third_max_number(self, nums: list[int]) -> int:
        if len(nums) == 0: return None
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > max1:                    
                max1, max2, max3 = num, max1, max2 
            if num > max2 and num < max1:
                max2, max3 = num, max2
            if num > max3 and num < max2:
                max3 = num        
        return max3 if max3 != float('-inf') else max1
    

if __name__ == "__main__":
    solver = ThirdMaximumNumberSolver()
    nums = [2,2,3,1]
    result = solver.third_max_number(nums)
    print(result)