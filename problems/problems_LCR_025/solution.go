package problemLCR_025

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
func reverseLinkedList(head *ListNode) *ListNode {
	var prev *ListNode
	curr := head
	for curr != nil {
		nextTemp := curr.Next
		curr.Next = prev
		prev = curr
		curr = nextTemp
	}
	return prev
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	l1 = reverseLinkedList(l1)
	l2 = reverseLinkedList(l2)

	var head *ListNode
	var carry int
	for l1 != nil || l2 != nil || carry > 0 {
		sum := carry
		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}
		carry = sum / 10
		sum = sum % 10
		head = &ListNode{Val: sum, Next: head}
	}
	return head
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var l1 *ListNode
	var l2 *ListNode

	var l1IntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &l1IntArray); err != nil {
		log.Fatal(err)
	}
	l1 = IntArrayToLinkedList(l1IntArray)
	var l2IntArray []int
	if err := json.Unmarshal([]byte(inputValues[1]), &l2IntArray); err != nil {
		log.Fatal(err)
	}
	l2 = IntArrayToLinkedList(l2IntArray)

	return LinkedListToIntArray(addTwoNumbers(l1, l2))
}
