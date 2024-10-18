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
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    
}

func Solve(inputJsonValues string) interface{} {
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
