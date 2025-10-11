/*
Valid Mountain Array
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Brute Force: Traversing through the loop from beginning to end
Continually check current elemnt < next element, until the peak
Once it starts decreasing, check continually current element > next element, until the end of the loop
This solution itself is optimal

Optimal solution: Two pointer
- Left pointer at beginning and right at end, left, right = 0, n-1, n is length of array
- First scan incrementing part o loop
	- if nums[left] < nums[left+1] and left < n-1, increment left, left++
- Scan decrementing part of loop
	- if nums[right] < nums[right-1], decrement right, right--
- Traverse through the loop until left<n-1 and right>0 and left<=right
	- if nums[left] < nums[left+1], increment left, left++
	// - else if nums[left]<nums[left+1] and left=n-1
	- if nums[right] < nums[right-1], decrement right, right--
return left == right

Time complexity: O(n)
Space complexity:0(1)

*/

package main

import "fmt"

func ValidMountainArray(arr []int) bool {
	n := len(arr)
	if n < 3 {
		return false
	}
	left, right := 0, n-1

	for left < n-1 && arr[left] < arr[left+1] {
		left++
	}

	for right > 0 && arr[right] < arr[right-1] {
		right--
	}
	if right == 0 || left == n-1 {
		return false
	}

	return left == right
}

func main() {
	arr := []int{0, 1, 2, 3, 2, 1}
	result := ValidMountainArray(arr)
	fmt.Printf("%v", result)
}
