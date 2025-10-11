"""
Container With Most Water
Medium
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

def maxArea(height: list[int]) -> int:
    maxArea = 0
    left, right = 0, len(height)-1
    
    while left < right:
        if height[left] < height[right]: 
            maxArea = max(maxArea, height[left] * (right-left))
            left += 1
        else:
            maxArea = max(maxArea, height[right] * (right-left))
            right -= 1
    
    return maxArea

"""
 0 1 2 3 4 5 6 7 8
[1,8,6,2,5,4,8,3,7]
left    right   h[left] h[right]    area    maxArea
0       8       1       7           1*6     6
1       8       8       7           7*7     49
"""
