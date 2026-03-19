"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:            
Input: s = "abcabcbb"   abccdec
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
"""
def longest_substring(s: str) -> int:
    start, max_len = 0, 0
    char_dict = {}
    
    for end, char in enumerate(s):
        if char in char_dict and start <= char_dict[char]:
            start = char_dict[char] + 1
        char_dict[char] = end
        max_len = max(max_len, end-start+1)
        
    return max_len

"""
Example iteration:
0123456
abccbec


start   end char    dict[char]  max_len
0       0   a       a:0         1
0       1   b       b:1         2
0       2   c       c:2         3
3       3   c       c:3         3
3       4   b       b:4         

"""