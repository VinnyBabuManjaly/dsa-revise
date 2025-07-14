"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Brute Force: For every character, loop through every character until a duplicate is found
Keeping track max length. time complexit: O(n^2)

Optimal: Sliding window approach
Keep two pointer, left and right = 0
Keep track of max length, intialized to 0
Initialize a char dictionary, to track existence of elements
Keeping left at the beginning, loop right from 0 to end for checking out possibilities.(keep track of index and value i the string)
    - for right, val in input string:
        - if val in char and char[val] >= left:
            left = char[val] + 1, i.e current index+1
        - char[val] = right
        - maxlen = max(maxlen, right-left+1)
return result

Time coplexity: O(n)
Space complexity: O(k) - Unique characters
"""
def longest_substring(s: str) -> int:
    left = 0
    char = {}
    maxLen = 0
    
    for right, val in enumerate(s):
        if val in char and char[val] >= left:
            left = char[val] + 1
        char[val] = right
        maxLen = max(maxLen, right - left + 1)
    
    return maxLen

