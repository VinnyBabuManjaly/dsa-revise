"""
Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Brute force is optimal:
Initialize variable to store result
Initialize a dictionary with roman letters and values as key and value respectively
Iterate over the string from beginning to n-2
Compare current element and next element, 
    -if s[i] >= s[i+1], result += s[i]
    -else, result -= s[i]
result += s[:i+1], adding the last element
    
Simulation with example:
     01234
s = "LVIII"
i   s[i]    s[i+1]  result
-   -       -       0
0   L       V       50
1   V       I       55
2   I       I       56
3   I       I       57       

Time: O(n)
Space: O(1)

Edge cases:
Empty string
One element string
Multiple element string
Normal case, numerals in decreasing order
Edge case, numerals with increasing and decreasing order, ie with 4,9,40,90,400,900

"""

def roman_to_integer(s: str) -> int:
    result = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]: 
            result -= roman[s[i]]
        else: 
            result += roman[s[i]]
    
    return result

if __name__ == '__main__':
    result = roman_to_integer(s="LVIII")
    print(result)
