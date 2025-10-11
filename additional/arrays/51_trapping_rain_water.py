"""
Trapping Rain Water
Hard
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

def trap(height: list[int]) -> int:
    trapped = 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped += right_max - height[right]
            right -= 1
    
    return trapped


"""
 0 1 2 3 4 5 6 7 8 9 10 11
[0,1,0,2,1,0,1,3,2,1,2, 1]

left    right   h[left] h[right]    lmax    rmax    trapped
0       11      0       1           0       -       -
1       11      1       1           -       1       -
1       10      1       2           -       2       -
1       9       1       1           -       -       1
1       8       1       2           1       -       -
2       8       0       2           -       -       1
3       8       2       2           -       2       -
3       7       2       3           2       -       -
4       7       1       3           -       -       1
5       7       0       3           -       -       2
6       7       1       3           -       -       1

"""