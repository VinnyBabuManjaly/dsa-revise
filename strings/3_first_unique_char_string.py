"""
First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.

Brute Force: 
For each character, traverse through the loop and count how many times that character occurs.
After checking till the end for count of a character, if its one return its index, else -1.

Optimal solution: Hashing
Initialize count dictionary
Store count of each character in count dictionary, by traversing through the string until the end.
Index doesnt matter at this point
Loop through char in input string s, 
    - count[char] increment
Loop through index and char in s again,
    - if count[char] = 1, return index
    
Time complexity: O(2n)= O(n)
Space complexity: O(1), 26 characters for lowercase

Edge cases:

"""

def unique_string(s:str) -> int:
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for index, char in enumerate(s):
        if count[char] == 1:
            return index
    
    return -1

if __name__ == "__main__":
    s = "loveleetcode"
    result = unique_string(s)
    print(result)