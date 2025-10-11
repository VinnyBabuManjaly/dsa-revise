/*
Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.

Brute force: Traversing from end of the string, and storing values one by one in a new string/array to give result

Optimal: Two pointer approach
Initialize two pointers, left=0 and right=n-1 where n=len(s)
While left<right,
	- swap between left and right values
	- increment left and decrement right
	(if there is a mid chracter, that wont be considered as required, since left=right)
Return s array

Time complexity: O(n) - Single pass
Space complexity: O(1) extra - Only constant number of additional variables

Edge cases:
Empty string
One element string
Two element string
Even number string
Odd number string
With white space
With symbols/special characters
Upper case
Lower case
Mixed case
Unicode
Long string

*/

package main

// import "fmt"

func ReverseString (s []rune) []rune {
	n := len(s)
	left, right := 0, n - 1
	for left < right {
		s[left], s[right] = s[right], s[left]
		left++
		right--
	}
	return s
}

// func main() {
// 	s := []rune("hello")
// 	output := ReverseString(s)
// 	fmt.Println(string(output))
// }
