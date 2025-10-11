"""
Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""
def minWindow(s: str, t: str) -> str:
    t_counter = {}
    window_counter = {}
    left, right = 0, 0
    min_window = float('inf')
    window_start, window_end = 0, 0
    
    for char in t:
        t_counter[char] = t_counter.get(char, 0) + 1
    need = len(t_counter)
    have = 0
        
    while left <= right and right < len(s):
        if s[right] in t_counter:
            window_counter[s[right]] = window_counter.get(s[right], 0) + 1
            if window_counter[s[right]] == t_counter[s[right]]:
                have += 1
        right += 1
    
        while have == need and left <= right:
            if right-left < min_window:
                    min_window = right-left
                    window_start = left
                    window_end = right
            if s[left] in t_counter:
                window_counter[s[left]] = window_counter.get(s[left], 0) - 1
                if window_counter[s[left]] < t_counter[s[left]]:
                    have -= 1
            left += 1
            
    return s[window_start:window_end] if min_window != float('inf') else ""
        