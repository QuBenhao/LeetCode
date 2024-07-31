package problem21

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
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := &ListNode{}
	for cur := dummy; list1 != nil || list2 != nil; cur = cur.Next {
		if list1 != nil && (list2 == nil || list2.Val >= list1.Val) {
			cur.Next = &ListNode{Val: list1.Val}
			list1 = list1.Next
		} else {
			cur.Next = &ListNode{Val: list2.Val}
			list2 = list2.Next
		}
	}
	return dummy.Next
}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var list1 *ListNode
	var list2 *ListNode

	var list1IntArray []int
	if err := json.Unmarshal([]byte(values[0]), &list1IntArray); err != nil {
		log.Fatal(err)
	}
	list1 = IntArrayToLinkedList(list1IntArray)
	var list2IntArray []int
	if err := json.Unmarshal([]byte(values[1]), &list2IntArray); err != nil {
		log.Fatal(err)
	}
	list2 = IntArrayToLinkedList(list2IntArray)

	return LinkedListToIntArray(mergeTwoLists(list1, list2))
}
