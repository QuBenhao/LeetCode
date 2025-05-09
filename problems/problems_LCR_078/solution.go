package problemLCR_078

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
	pq := &IntHeap{}
	heap.Init(pq)
	for _, head := range lists {
		if head == nil {
			continue
		}
		heap.Push(pq, tuple{Val: head.Val, node: head})
	}
	dummy := &ListNode{}
	cur := dummy
	for pq.Len() > 0 {
		t := heap.Pop(pq).(tuple)
		cur.Next = t.node
		cur = cur.Next
		if t.node.Next != nil {
			t.node = t.node.Next
			t.Val = t.node.Val
			heap.Push(pq, t)
		}
	}
	return dummy.Next
}

type tuple struct {
	Val  int
	node *ListNode
}
type IntHeap []tuple

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i].Val < h[j].Val }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(tuple))
}
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func Solve(inputJsonValues string) interface{} {
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
