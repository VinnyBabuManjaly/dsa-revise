"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:
string encoded_string = encode(strs);
and Machine 2 does:
vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.
Implement the encode and decode methods.
You are not allowed to solve the problem using any serialize methods (such as eval).

Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2
Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:
Input: dummy_input = [""]
Output: [""]

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
"""
from typing import List

class Codec:
    def encode(strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)
    
    def decode(s: str) -> List[str]:
        i = 0
        result = []
        
        while i < len(s):
            j = i
            
            # Extract length
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            # Exclude '#'
            j += 1
            
            # Extarct string and append to result
            result.append(s[j:j+length])
            i = j + length
            
        return result
    
""" 
 012345678910111213 
"5#hello5#wo r l d"
i   j   length  string
0   0   -       -
0   1   5       -
0   2   5       s[2:7]=hello
7   7   -       -
7   8   5       -
7   9   5       s[9:14]

""" 