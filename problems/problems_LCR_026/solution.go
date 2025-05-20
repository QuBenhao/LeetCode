package problemLCR_026

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
func reorderList(head *ListNode) {
	n := 0
	cur := head
	for cur != nil {
		n++
		cur = cur.Next
	}
	mid := (n + 1) / 2
	midNode := head
	for i := 0; i < mid-1; i++ {
		midNode = midNode.Next
	}
	reservedHead := midNode.Next
	midNode.Next = nil
	cur = reservedHead
	for cur != nil && cur.Next != nil {
		next := cur.Next
		cur.Next = next.Next
		next.Next = reservedHead
		reservedHead = next
	}

	cur = head
	for reservedHead != nil {
		next := cur.Next
		cur.Next = reservedHead
		rNext := reservedHead.Next
		reservedHead.Next = next
		cur = next
		reservedHead = rNext
	}
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var head *ListNode

	var headIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedList(headIntArray)

	reorderList(head)
	return LinkedListToIntArray(head)
}
