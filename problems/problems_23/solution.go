package problem23

import (
	"container/heap"
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
	h := hp{}
	for _, head := range lists {
		if head != nil {
			h = append(h, head)
		}
	}
	heap.Init(&h) // Heapify

	dummy := &ListNode{} // Sentinel node preceding the head of the merged list
	cur := dummy
	for len(h) > 0 { // Loop until the heap is empty
		node := heap.Pop(&h).(*ListNode) // Smallest remaining node
		if node.Next != nil {            // The next node is not null
			heap.Push(&h, node.Next) // The next node may be the smallest; push it onto the heap
		}
		cur.Next = node // Merge into the new list
		cur = cur.Next  // Prepare to merge the next node
	}
	return dummy.Next // The node after the sentinel is the head of the new list
}

type hp []*ListNode

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].Val < h[j].Val } // Min-heap
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(*ListNode)) }
func (h *hp) Pop() any          { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var lists []*ListNode

	var listsIntArrays [][]int
	if err := json.Unmarshal([]byte(inputValues[0]), &listsIntArrays); err != nil {
		log.Fatal(err)
	}
	for i := 0; i < len(listsIntArrays); i++ {
		lists = append(lists, IntArrayToLinkedList(listsIntArrays[i]))
	}

	return LinkedListToIntArray(mergeKLists(lists))
}
