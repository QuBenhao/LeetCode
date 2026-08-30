package problem2058

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
func nodesBetweenCriticalPoints(head *ListNode) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var head *ListNode

	var headIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedList(headIntArray)

	return nodesBetweenCriticalPoints(head)
}
