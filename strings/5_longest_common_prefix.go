/*
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

Brute Force: Compare characters in every string at the same time
Vertical scanning. With mismatch return string from index 0 to the respective prefix

Optimal solution: Horizontal scanning
Keeping prefix as first element in the input strings
Starting from the second element and looping until the end of input array.
	Check if prefix == element: break out of the loop
		else: prefix = prefix[:len(prefix)-1], reducing length of prefix
		if prefix == "", return ""(no match)
Return prefix after all elements are matched for the prefix

Time complexity: O(n)
Space complexity: O(1)

Edge cases:
Empty input array
One elemnt array
All elements match
No prefix match at all
First elements match
All same elements in array
Empty string in array out of many elemnts

Maximum length input array
*/

package main

import (
	"fmt"
	"strings"
)

type CommonPrefixSolver struct{}

func (cp *CommonPrefixSolver) CommonPrefix (strs []string) string {
	prefix := strs[0]
	for _, s := range strs[1:] {
		for !strings.HasPrefix(s, prefix) {
			if prefix == "" { return ""}
			prefix = prefix[:len(prefix)-1]
		}
	}
	return prefix
}

func main () {
	cp := CommonPrefixSolver{}
	strs := []string{"flower", "flow", "flight"}
	result := cp.CommonPrefix(strs)
	fmt.Println(result)
}
