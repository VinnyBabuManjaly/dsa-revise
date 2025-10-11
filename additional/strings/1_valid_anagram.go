/*
Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Brute Force: Check if length of both strings are equal. Sort strings and compare. time complexity: O(nlogn)

Optimal approach: Hashmap
Initialize dictionaries to count frequencies of alphabets in both strings.
Traverse through two strings at the same time.
	- 
Compare two frquency maps

*/
package main

// import "fmt"

func valid_anagram(s string, t string) bool {
	smap := make(map[rune]int)

	if len(s) != len(t) {
		return false
	}
	
	for _, char := range s {
		smap[char]++
	}
	for _, char := range t {
		if smap[char] == 0 {
			return false
		}
		smap[char]--
	}

	return true
}

// func main() {
// 	s := "anagram"
// 	t := "nagaram"
// 	result := valid_anagram(s, t)
// 	fmt.Printf("%v", result)
// }