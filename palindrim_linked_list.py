# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    fast, slow, prev = head, head, None
    while fast and fast.next:
        fast = fast.next.next
        slow, prev.next, prev = slow.next, prev, slow

    if fast:
        slow = slow.next

    while prev:
        if slow.val != prev.val:
            return False

    return True

