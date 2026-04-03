class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListSolutions:
    # 1. Linked List Cycle (Floyd's Tortoise and Hare)
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False

    # 2. Add Two Numbers
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            curr.next = ListNode(val % 10)
            curr, l1, l2 = curr.next, (l1.next if l1 else None), (l2.next if l2 else None)
        return dummy.next

    # 3. Merge Two Sorted Lists
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next

    # 4. Reverse Linked List II (Partial Reverse)
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1): prev = prev.next
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next

    # 5. Remove Nth Node From End of List
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n -= 1
        while right:
            left, right = left.next, right.next
        left.next = left.next.next
        return dummy.next
