package double_linked_node_child

// Definition for a Node.
type Node struct {
	Val   int
	Prev  *Node
	Next  *Node
	Child *Node
}

func IntArrayToDoubleLinkedNode(arr []any) *Node {
	if len(arr) == 0 {
		return nil
	}
	head := &Node{arr[0].(int), nil, nil, nil}
	curr := head
	currHead := head
	for idx, n := 1, len(arr); idx < n; idx++ {
		isChild := false
		if arr[idx] == nil {
			curr = currHead
			isChild = true
			idx++
		}
		for arr[idx] == nil {
			if curr != nil {
				curr = curr.Next
			}
			idx++
		}
		if isChild {
			curr.Child = &Node{arr[idx].(int), nil, nil, nil}
			curr = curr.Child
			currHead = curr
		} else {
			curr.Next = &Node{arr[idx].(int), curr, nil, nil}
			curr = curr.Next
		}
	}
	return head
}

func DoubleLinkedNodeToIntArray(head *Node) (ans []any) {
	currHead, curr := head, head
	var nxt *Node
	for curr != nil || nxt != nil {
		if curr == nil {
			curr = currHead
			ans = append(ans, nil)
			for curr.Child != nxt {
				curr = curr.Next
				ans = append(ans, nil)
			}
			curr = nxt
			currHead = nxt
			nxt = nil
		}
		if curr.Child != nil {
			nxt = curr.Child
		}
		ans = append(ans, curr.Val)
		curr = curr.Next
	}
	return
}
