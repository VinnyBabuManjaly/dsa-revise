"""
Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Brute Force: Nested loop
For each element nums[i] it check for eelments from beginning nums[0] to nums[i-1] if the element already exists.
If not store at location k, which tracks the unique number of elements after processing

Optimal solution: Two pointer
A read pointer to scan all the elements and see if previous element is same as the current element
A write pointer that tracks the unique number of elements, and also used as a reference to write unique element in place to the nums array 
condition to be checked: nums[read] == nums[read-1]
    - if not equal, then update the value at write pointer to the found unique element(nums[write] as nums[read]) and increment write pointer by 1
increment the read pointer to the next element
return 
    - k = write +1
    - nums

Time complexity: O(n)
Space complexity: O(1)


Simulation:
        0 1 2 3 4 5 6 7 8 9
nums = [0,0,1,1,1,2,2,3,3,4]
read    write   nums[read]  nums[read-1]    condition   nums[write]     nums
1       1       0           0               equal       -               [0,....]
2       1       1           0               not equal   1               [0, 1,...]
3       2       1           1               equal       -               [0, 1,...]
4       2       1           1               equal       -               [0, 1,...]
5       2       2           1               not equal   2               [0, 1, 2,...]
"""

class RemoveDuplicatesSolver():
    def remove_duplicates(self, nums: list[int]) -> tuple[int, list[int]]:
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read-1]:
                nums[write] = nums[read]
                write += 1
        return write, nums[:write]
    

if __name__ == "__main__":
    solver = RemoveDuplicatesSolver()
    nums = [0]
    k, results = solver.remove_duplicates(nums)
    print(k, results)
