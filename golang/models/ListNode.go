package models

type ListNode struct {
	Val  int
	Next *ListNode
}

func IntArrayToLinkedList(arr []int) *ListNode {
	dummy := &ListNode{}
	node := dummy
	for _, v := range arr {
		node.Next = &ListNode{Val: v}
		node = node.Next
	}
	return dummy.Next
}

func LinkedListToIntArray(listNode *ListNode) (arr []int) {
	for node := listNode; node != nil; node = node.Next {
		arr = append(arr, node.Val)
	}
	return arr
}

func IntArrayToLinkedListCycle(arr []int, pos int) *ListNode {
	if len(arr) == 0 || pos == -1 {
		return IntArrayToLinkedList(arr)
	}
	dummy := &ListNode{}
	node := dummy
	var cycleNode *ListNode
	for i := 0; i < len(arr); i++ {
		node.Next = &ListNode{Val: arr[i]}
		node = node.Next
		if i == pos {
			cycleNode = node
		}
	}
	node.Next = cycleNode
	return dummy.Next
}

func IntArrayToLinkedListIntersection(arr1, arr2 []int, iv, idx1, idx2 int) []*ListNode {
	if iv == 0 {
		return []*ListNode{IntArrayToLinkedList(arr1), IntArrayToLinkedList(arr2)}
	}
	dummy1, dummy2 := &ListNode{}, &ListNode{}
	node1, node2 := dummy1, dummy2
	for i := 0; i < idx2; i++ {
		node2.Next = &ListNode{Val: arr2[i]}
		node2 = node2.Next
	}
	for i := 0; i < len(arr1); i++ {
		node1.Next = &ListNode{Val: arr1[i]}
		node1 = node1.Next
		if i == idx1 {
			node2.Next = node1
		}
	}
	return []*ListNode{dummy1.Next, dummy2.Next}
}
