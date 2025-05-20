package node_random

import "log"

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func IntRandomArrayToNodeArray(nums [][]any) *Node {
	var record []*Node
	dummy := &Node{}
	node := dummy
	for _, arr := range nums {
		node.Next = &Node{Val: int(arr[0].(float64))}
		node = node.Next
		record = append(record, node)
	}
	for idx, arr := range nums {
		if arr[1] != nil {
			record[idx].Random = record[int(arr[1].(float64))]
		}
	}
	return dummy.Next
}

func NodeArrayToIntRandomArray(head *Node) (ans []any) {
	idxMap := map[*Node]int{}
	node := head
	for i := 0; node != nil; i++ {
		idxMap[node] = i
		node = node.Next
	}
	node = head
	for node != nil {
		if node.Random != nil {
			if v, ok := idxMap[node.Random]; ok {
				ans = append(ans, []any{node.Val, v})
			} else {
				log.Fatal("Invalid node with random, check input!")
			}
		} else {
			ans = append(ans, []any{node.Val, nil})
		}
		node = node.Next
	}
	return
}
