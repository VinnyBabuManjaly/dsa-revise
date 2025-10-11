"""
Maximum Product of Two Elements in an Array
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
Constraints:
2 <= nums.length <= 500
1 <= nums[i] <= 10^3

Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

Brute force: Nested loops
For each element multiply with each element in the array and track max product. Return max product
Sort first and return product of last two elements

Optimal solution:
Largest product is the product of largest numbers in the array
Initialize first and second variables to '-inf'/none, to track first and second largest numbers in the array respectively
Track two largest numbers in a single pass
    - Loop until the end of array, index doesn't matter
    - if num>first, (first, second = num, first)
    - if num>second and num<first, second = num
Return (first - 1) * (second - 1)

Simulation with example:
 0 1 2 3
[3,4,6,5]
num first   sec
    -inf    -inf    (input)
    6       5       (expected)
3   3       -inf
4   4       3
6   6       4
5   6       5


"""

def max_product(nums: list[int]) -> int:
    first = second = float('-inf')
    for num in nums:
        if num > first: first, second = num, first
        elif num > second: second = num
    return (first - 1) * (second - 1)

if __name__ == "__main__":
    nums = [3,4,6,5]
    result = max_product(nums)
    print(result)
    