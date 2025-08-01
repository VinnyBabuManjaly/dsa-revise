"""
Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:          
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import defaultdict

def group_annagrams(strs: list) -> list:
    result = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char)-ord('a')] += 1
        count_tuple = tuple(count)
        result[count_tuple].append(word)
    return list(result.values())    
    
"""
Example

strs = ["eat","tea","tan","ate","nat","bat"]
word   tuple    result
eat    [1,0]*26 

"""        