package problemLCR_078

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
func mergeKLists(lists []*ListNode) *ListNode {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var lists []*ListNode

	var listsIntArrays [][]int
	if err := json.Unmarshal([]byte(inputValues[0]), &listsIntArrays); err != nil {
		log.Fatal(err)
	}
	for i := 0; i < len(listsIntArrays); i++{
		lists = append(lists, IntArrayToLinkedList(listsIntArrays[i]))
	}

	return LinkedListToIntArray(mergeKLists(lists))
}
