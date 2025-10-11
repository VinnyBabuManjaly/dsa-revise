/*
Find Numbers with Even Number of Digits
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: Only 12 and 7896 contain an even number of digits.

Brute Force: Taking numbers in array one by one and checking how many times its divisible by 10 to calculate the number of digits
Incrementing result counter if the number of digits is even

Optimal solution:
Taking numbers in array one by one and converting string to count the number of digits.
With even number of digits keep incrementing the result counter to give the total numbers with even number of digits.

Simulation with example:
Time complexity: O(n)
Space complexity: O(1)
Edge cases:
*/

package main

import (
	// "fmt"
	"strconv"
)

type DigitAnalyzer struct{}

func (da *DigitAnalyzer) EvenDigitNumbers(nums []int) int {
	result := 0
	for _, num := range nums {
		if len(strconv.Itoa(abs(num)))%2 == 0 {
			result++
		}
	}
	return result
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

// func main() {
// 	nums := []int{-12,345,2,6,7896}
// 	analyzer := DigitAnalyzer{}
// 	result := analyzer.EvenDigitNumbers(nums)
// 	fmt.Printf("%v", result)
// }
