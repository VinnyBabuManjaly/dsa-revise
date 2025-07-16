"""
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

ARCHITECT
"""
def valid_anagram(s: str, t:str) -> bool:
    if len(s) != len(t): return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    for char in t:
        if not count.get(char, 0):
            return False
        count[char] -= 1
    return True
         

"""
Example:
s = "anagram", t = "nagaram"

char    count[char]
a       {a:1}
n
a
g
r
a
m       {a:3, n:1, g:1, r:1, m:1}

char    count[char] count
n       1           n:0
a       3           a:2
g       1           g:0
a       2           a:1
r       1           r:0
a       1           a:0
m       1           m:0

"""

if __name__ == "__main__":
    print(valid_anagram(s = "anagram", t = "nagaram"))
        
            
