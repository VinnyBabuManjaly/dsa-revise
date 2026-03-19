"""
Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Brute force:
n nested loops to bring all zeroes to end, where n is length of the array
During each if the current element is 0 and the next elemnt is not zero, the values are interchanged
time complexity - o(n^2)

Optimal solution: Two pointer
- Initialize 
    -write pointer at 0 that is beginning
- Loop over the element with read pointer until the end of the array
    - whenever current element at read pointer is not zero, write the current element to the nums array at the write pointer
        - nums[write] = nums[read]
        - increment write pointer
    - whenever current element is zero, ignore it 
    - increment the read pointer
- If the read pointer reaches the end of array, i.e while write poiner may still be not at the end
    - while write<len(nums)
        - increment write pointer
        -append zero to the nums array at write pointer, i.e. nums [write] = 0
- return nums

Simulation for example:
condition: nums[read] != 0
 0 1 2 3 4 
[0,1,0,3,12]
read    write   nums[read]  nums[write] condition   nums            
0       0       0           0           -           [0,1,0,3,12]
1       0       1           1           valid       [#1,1,0,3,12]
2       1       0           1           -           [1,1,0,3,12]
3       1       3           3           valid       [1,#3,0,3,12]
4       2       12          12          valid       [1,3,#12,3,12]
-
-       3       -           0           -           [1,3,12,#0,12]


Time Complexity: O(n)
Space Complexity: O(1)
Edge cases:

"""

class MoveZeroesSolver():
    def move_zeroes(self, nums: list[int]) -> list[int]:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0: 
                nums[write] = nums[read]
                write += 1
        while (write < len(nums)):
            nums[write] = 0
            write += 1
        
        return nums
    

if __name__ == "__main__":
    solver = MoveZeroesSolver()
    nums = [0,1,0,3,12]
    result = solver.move_zeroes(nums)
    print(result)
