import solution
from typing import *
from object_libs import list_to_linked_list, call_method
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = S(list_to_linked_list(*inputs[0]))
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class S:
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        # nums = []
        # node = self.head
        # while node:
        #     nums.append(node.val)
        #     node = node.next
        # return random.choice(nums)

        # solve a very long list without using extra space
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value
