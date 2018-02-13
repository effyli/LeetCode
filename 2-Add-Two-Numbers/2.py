# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            p = q = 0
            if l1:
                p = l1.val
                l1 = l1.next
            if l2:
                q = l2.val
                l2 = l2.next
            n.next = ListNode((p+q+carry)%10)
            if (p + q + carry) > 9:
                carry = 1
            else:
                carry = 0
            n = n.next

        return root.next


# following codes are from https://github.com/pezy/LeetCode/blob/master/001.%20Add%20Two%20Numbers/solution.py
def compareLinkedList(l1, l2):
    while l1 or l2:
        if not (l1 and l2) or l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return True


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    lsum = ListNode(7)
    lsum.next = ListNode(0)
    lsum.next.next = ListNode(8)
    print(compareLinkedList(Solution().addTwoNumbers(l1, l2), lsum))

# l1 = [2,4,3]
# l2 = [5,6,4]
# print(Solution.addTwoNumbers(Solution.addTwoNumbers,l1,l2))