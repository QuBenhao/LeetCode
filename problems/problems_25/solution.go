package problem25

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
func reverseKGroup(head *ListNode, k int) *ListNode {
	if head == nil {
		return nil
	}
	node := head
	for i := 0; i < k-1; i++ {
		if node == nil {
			break
		}
		node = node.Next
	}
	if node == nil {
		return head
	}
	node.Next = reverseKGroup(node.Next, k)
	tail := node.Next
	last := tail
	for head != last {
		nxt := head.Next
		head.Next = tail
		tail = head
		head = nxt
	}
	return node
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var head *ListNode
	var k int

	var headIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedList(headIntArray)
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return LinkedListToIntArray(reverseKGroup(head, k))
}
