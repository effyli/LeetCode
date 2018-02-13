# Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

# Solution
This is my first try about linked list in python

The core idea is to remember that every node contains two things: value and pointer(to next node).

As for this question:
1. Add a variable called carry to note if there is a carry when sum two digits.
2. When calculate the digits, need to consider if carry is 1.
3. Could use divmod function to get the div and mod.

Linked list in python is kind of tricky because it needs to denote the head, value and next.