package problem1290

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
func getDecimalValue(head *ListNode) (ans int) {
	for node := head; node != nil; node = node.Next {
		ans <<= 1
		ans |= node.Val
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var head *ListNode

	var headIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedList(headIntArray)

	return getDecimalValue(head)
}
