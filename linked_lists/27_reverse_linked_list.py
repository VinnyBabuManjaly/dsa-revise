"""
Reverse Linked List
Easy
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


            head -------> node1 -------> node2 -------> node3 -------> node4

prev=None              
curr=head
next_n

"""

from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head
        
            
            
"""
    prev    head -> n1 -> n2 -> n3
    
    
                1 ->        2 ->        3 ->        4 ->        5 -> None
                5 <-        4 <-        3 <-        2 <-        1 
newhead                     5           5                       5
head.next                   5           4                       2 
head                        4           3                       1

head.next.next              5->4        4->3        3->2        2->1
head.next                   4-None      3->None     2->None     1->None
"""