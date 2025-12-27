package problemInterview_02__03

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
func deleteNode(node *ListNode) {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var node *ListNode

	var nodeIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &nodeIntArray); err != nil {
		log.Fatal(err)
	}
	 var nodePos int
	if err := json.Unmarshal([]byte(inputValues[1]), &nodePos); err != nil {
		log.Fatal(err)
	}
	node = IntArrayToLinkedListCycle(nodeIntArray, nodePos)

	deleteNode(node)
	return LinkedListToIntArray(node)
}
