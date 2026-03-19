"""
Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

Brute force:
Take characters one by one from ransomnote, and check if it exists in magazine, by scanning through magazine chars one by one
If found check for next character, if not found, return false. Return true at end

Optimal solution: Hashmap and freq counting
Count character frequency for all characters in magazine. (One loop through magazine)
One loop through ransomnote, check if chars in ransomnote exists(one by one)
    - if count = 0/is not present, return false
    - else decrement char frequency count by 1
return true

Time complexity: O(m+n)
Space complexity: O(1)

ransomNote = "aa", magazine = "aab"
Edge cases:
Empty ransomenote
Empty magazine
Empty ransomnote and magazine
Equal length
Same ransomenpote and same magazine
Multiple same character in ransomnote, only one in magaazine
Normal tru case
Normal false case

"""
from collections import Counter

class RansomeNoteSolver:
    def ransom_note(self, ransomNote: str, magazine: str) -> bool:
        freq = Counter(magazine)
        for char in ransomNote:
            if freq.get(char, 0) == 0:
                return False
            freq[char] -= 1
        return True