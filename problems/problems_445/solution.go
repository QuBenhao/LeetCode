package problem445

import (
	"encoding/json"
	. "leetCode/golang/models"
	"log"
	"strings"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var reverseList func(node *ListNode) *ListNode
	reverseList = func(node *ListNode) *ListNode {
		if node == nil || node.Next == nil {
			return node
		}
		newHead := reverseList(node.Next)
		node.Next.Next = node
		node.Next = nil
		return newHead
	}
	dummy := &ListNode{}
	l1r, l2r := reverseList(l1), reverseList(l2)
	for cur, node := 0, dummy; l1r != nil || l2r != nil || cur > 0; cur /= 10 {
		if l1r != nil {
			cur += l1r.Val
			l1r = l1r.Next
		}
		if l2r != nil {
			cur += l2r.Val
			l2r = l2r.Next
		}
		node.Next = &ListNode{Val: cur % 10}
		node = node.Next
	}
	return reverseList(dummy.Next)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var l1 *ListNode
	var l2 *ListNode

	var l1IntArray []int
	if err := json.Unmarshal([]byte(values[0]), &l1IntArray); err != nil {
		log.Fatal(err)
	}
	l1 = IntArrayToLinkedList(l1IntArray)
	var l2IntArray []int
	if err := json.Unmarshal([]byte(values[1]), &l2IntArray); err != nil {
		log.Fatal(err)
	}
	l2 = IntArrayToLinkedList(l2IntArray)

	return LinkedListToIntArray(addTwoNumbers(l1, l2))
}
