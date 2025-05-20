package problem2181

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
func mergeNodes(head *ListNode) *ListNode {
	dummy := &ListNode{Val: 0}
	node, cur := dummy, head.Next
	for cur != nil {
		s := 0
		for cur != nil && cur.Val != 0 {
			s += cur.Val
			cur = cur.Next
		}
		node.Next = &ListNode{Val: s}
		node = node.Next
		if cur != nil {
			cur = cur.Next
		}
	}
	return dummy.Next
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var head *ListNode

	var headIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedList(headIntArray)

	return LinkedListToIntArray(mergeNodes(head))
}
