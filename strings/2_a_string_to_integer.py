"""
String to Integer (atoi)
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Input: s = "-001337c0d3"
Output: -1337


Brute force and optimal: Check for conditions one by one
Loop from 0 to n-1 of string with variable i
1. Check for leading white spaces, ignore and increment
1a. Check for sign, in sign variable store -1 or 1 respective to the sign if exists and increment i
1b. Check for zeroes after sign, ignore and increment
2. Check if digit and keep adding to result until end or not a digit 
3.a If no digits return zero
4. Convert result string to integer and check if within range range [-231, 231 - 1], return values respectively

Edge cases:
-0004   4
0-1     0
"""

def string_to_integer(s:str) -> int:
    result = ""
    sign = 1
    
    i = 0
    if i < len(s) and (s[0] == "-" or s[0] == "+"): 
        sign = -1 if s[0] == "-" else 1
        i += 1
    
    while i < len(s) and (s[i] == "0" or s[i] == " "):
        i += 1
    
    while(i < len(s) and s[i].isdigit()):
        result += s[i]
        i += 1
        
    if int(result) < 2**31 - 1 and sign == 1: result = 2**31 - 1
    if int(result) < 2**31 and sign == -1: result = 2**31
        
    return sign * int(result)