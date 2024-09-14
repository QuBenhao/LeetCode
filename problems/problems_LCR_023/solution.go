package problemLCR_023

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
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	nodeA, nodeB := headA, headB
	for nodeA != nodeB {
		if nodeA == nil {
			nodeA = headB
		} else {
			nodeA = nodeA.Next
		}
		if nodeB == nil {
			nodeB = headA
		} else {
			nodeB = nodeB.Next
		}
	}
	return nodeA
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var iv, idx1, idx2 int
	var headA, headB *ListNode
	if err := json.Unmarshal([]byte(inputValues[0]), &iv); err != nil {
		log.Fatal(err)
	}
	var headAIntArray []int
	if err := json.Unmarshal([]byte(inputValues[1]), &headAIntArray); err != nil {
		log.Fatal(err)
	}
	var headBIntArray []int
	if err := json.Unmarshal([]byte(inputValues[2]), &headBIntArray); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &idx1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &idx2); err != nil {
		log.Fatal(err)
	}
	heads := IntArrayToLinkedListIntersection(headAIntArray, headBIntArray, iv, idx1, idx2)
	headA, headB = heads[0], heads[1]

	return LinkedListToIntArray(getIntersectionNode(headA, headB))
}
