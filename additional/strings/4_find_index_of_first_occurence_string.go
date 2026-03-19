/*
Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Brute Force: Check for occurence of needle at every index of haystack.
If the first character in needle matches, the current element in haystack, compare the rest of characters in needle
Time complexity: O(hn) h-lenth of haystack, n-lenth of needle

Optimal solution: Sliding window(brute force only)
Window length is length of needle
- Loop over haystack in the range of h-n-1 using start variable denoting a window start
		- check if haystack[start:start+n] == needle, if yes return start
return -1
 
 012345678   012
"sadbutsad" "sad"
h=9	n=3
Loop from 0 to 7(excluding 7, until 6)
7 = 9-3+1, i.e h-n+1

Time complexity: O(mn)
Space complexity: O(1)	

Edge cases:
Normal with match
Normal no match
Empty haystack
Empty needle
Empty haystack and needle
One element haystack
One element needle
haystack=needle
needle longer than haystack
needle at end
haystack with maximum length=104
needle with maximum length=104

*/

package main

// import "fmt"

func FirstOccurence(haystack string, needle string) int {
	h, n := len(haystack), len(needle)
	if h == 0 || n == 0 {
		return -1
	}
	start := 0
	for start < h - n + 1 {
		if haystack[start:start+n] == needle {
			return start
		}
		start++
	}
	return -1
}

// func main() {
// 	haystack := "sadbutsad" 
// 	needle := "sad"
// 	result := FirstOccurence(haystack, needle)
// 	fmt.Println(result)
// }