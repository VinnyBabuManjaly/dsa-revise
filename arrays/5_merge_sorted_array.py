"""
Merge Sorted Array
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Brute Force: 
- Merge two arrays ignoring sort
- Sort the result in an additional array
- Copying the results to the nums1
Inefficient time complexity = O(nlogn + mlogm), space complexity = O(m+n)

Optimal Solution:Two pointer technique
Initialize, 
    - a write pointer at the end of nums1, p = (m+n-1)
    - read pointers at valid ends of both arrays
        - read1= m-1
        - read= n-1
Looping from the ends of both arrays with valid numbers(not zeroes)
    - in nums2 starting from m-1th position
    - in nums2 starting from n-1th position
    looping done while m>=0 and n>=0 and p>=0
        - if nums1[read1] >= nums2[read2]:
            nums1[p] = nums1[read1]
            read1 -= 1
        - else 
            nums1[p] = nums2[read2]
            read2 -= 1
        decrement write pointer p by 1
    while n>=0 and p>=0
     - we are not considering m>=0 condition, since the values are being changed in place in nums1 and m in the lenght of nums1 itself, values/elements would already be there in the nums1 array and need not merge again
     - but if the are still values left to be read in nums2, those have to be merged to beginning of nums1 array directly without checking for any condition
     - nums1[p] = nums2[read2] 
     - decrement both p and read2 by 1 each time
return nums1


Simulation with example:
condition: nums1[read1] >= nums2[read2]
         0 1 2 3 4 5 6                  0 1 2
nums1 = [1,2,3,4,0,0,0], m = 4, nums2 = [2,5,6], n = 3
p   read1   read2   nums1[read1]    nums2[read2]    condition   nums1[p]    nums1
6   3       2       4               6               false       6           [1,2,3,4,0,0,#6]
5   3       1       4               5               false       5           [1,2,3,4,0,#5,6]
4   3       0       4               2               true        4           [1,2,3,4,#4,5,6]
3   2       0       3               2               true        3           [1,2,3,#3,4,5,6]
2   1       0       2               2               true        2           [1,2,#2,3,4,5,6]
1   0       0       1               2               false       2           [1,#2,2,3,4,5,6]
0   0       -1      

Time Complexity: O(m+n)
Space Complexity: O(1)
"""

class MergeSortedArraySolver():
    def merge_sorted_array(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
        write = m + n - 1
        read1 = m - 1
        read2 = n - 1

        while(write >= 0 and read1 >= 0 and read2 >= 0):
            if nums1[read1] >= nums2[read2]:
                nums1[write] = nums1[read1]
                read1 -= 1
            else:
                nums1[write] = nums2[read2]
                read2 -= 1
            write -= 1
        
        while (read2>=0 and write>=0):
            nums1[write] = nums2[read2]
            read2 -= 1
            write -= 1

        return nums1


if __name__ == "__main__":
    solver = MergeSortedArraySolver()
    nums1 = [1,2,3,0,0,0,0,0]
    m = 3
    nums2 = [2,2,5,6,8]
    n = 5
    result = solver.merge_sorted_array(nums1, m, nums2, n)
    print(result)