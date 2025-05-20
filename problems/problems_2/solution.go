package problem2

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
	dummy := &ListNode{}
	node := dummy
	for addition := 0; l1 != nil || l2 != nil || addition != 0; node = node.Next {
		cur := addition
		if l1 != nil {
			cur += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			cur += l2.Val
			l2 = l2.Next
		}
		node.Next = &ListNode{Val: cur % 10}
		addition = cur / 10
	}
	return dummy.Next
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
