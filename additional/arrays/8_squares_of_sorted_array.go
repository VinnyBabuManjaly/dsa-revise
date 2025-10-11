/*
Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Brute force: Calculating the squares of each numbers and sorting the array of squared numbers. Time compexity O(n log n)

Optimal solution: Two pointer approach(Not in place solution)
- Initialize
	- Result array of length n, which is the length same as that of the input itself
	- Left at beginning, left = 0
	- Right pointer at end, right = n-1
	- Index pointer to write the results, index = n-1
- Check if absolute values of nums[right] >= nums[left]
	- result[index] = nums[riight] * nums[right]
	- right-- (decrement)
- else
	- result[index] = nums[left] * nums[left]
	- left++ (increment)
- index-- (decrement)

Simulation with example:
condition: nums[right] >= nums[left]
  0  1 2 3 4
[-4,-1,0,3,10]
left	right	nums[left]	nums[right]	condition	result[index]	result
0		4		-4			10			true		100				[0,0,0,0,100]
0		3		-4			3			false		16				[0,0,0,16,100]
1		3		-1			3			true		9				[0,09,16,100]

Time complexity: O(n)
Space complexity: O(n)

Edge cases:
*/
package main

// import (
// 	"fmt"
// )

type SquareSolver struct{}

func (sq *SquareSolver) SquaresOfSortedArray(nums []int) []int {
	n := len(nums)
	result := make([]int, n)
	left, right, index := 0, n-1, n-1

	for left <= right {
		if abs(nums[right]) >= abs(nums[left]) {
			result[index] = nums[right] * nums[right]
			right--
		} else {
			result[index] = nums[left] * nums[left]
			left++
		}
		index--
	}
	return result
}

// func main () {
// 	solver := SquareSolver{}
// 	nums := []int{1, 1, 1}
// 	result := solver.SquaresOfSortedArray(nums)
// 	fmt.Println(result)
// }
