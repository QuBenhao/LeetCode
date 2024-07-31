package problem206

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
func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	newHead := reverseList(head.Next)
	head.Next.Next = head
	head.Next = nil
	return newHead
}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var head *ListNode

	var headIntArray []int
	if err := json.Unmarshal([]byte(values[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedList(headIntArray)

	return LinkedListToIntArray(reverseList(head))
}
