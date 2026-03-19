"""
Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true
Example 2:
Input: word = "FlaG"
Output: false

Brute force and optimal same:
- Loop over the word
    - Check upper count with 'A' <= char <='Z'
Three conditions to check:
    - All upper: if upper count = len of word
    - All lower: if upper count = 0
    - First upper and rest lower, if word[0] is upper and upper count = 1  
    
Time complexity: O(n)
Space complexity: O(1)

Constraints:
1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""

class DetectCapitalSolver():
    def detect_capital(self, word: str) -> bool:
        def is_upper(char: str):
            return 'A' <= char <= 'Z'
        
        upper_count = 0
        for char in word:
            if is_upper(char):
                upper_count += 1
        
        if upper_count == len(word) or upper_count == 0 or (is_upper(word[0]) and upper_count == 1):
            return True
        return False
    
if __name__ == "__main__":
    solver = DetectCapitalSolver()
    words = ["USA", "leetcode", "Google", "FlaG", "A", "mL"]
    for word in words:
        print(f"{word}\t: {solver.detect_capital(word)}")
        