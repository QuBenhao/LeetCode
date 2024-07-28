package tree_next

import (
	"encoding/json"
	"log"
)

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func ArrayToTreeNext(input string) *Node {
	var value interface{}
	if err := json.Unmarshal([]byte(input), &value); err != nil {
		log.Fatalf("Unable to process tree input: %s", input)
		return nil
	}
	arr := value.([]interface{})
	if len(arr) == 0 {
		return nil
	}
	var root *Node
	if arr[0] == nil {
		return nil
	} else {
		root = &Node{Val: int(arr[0].(float64))}
	}
	isLeft := 1
	var nodes []*Node
	currNode := root
	for i := 1; i < len(arr); i++ {
		var node *Node
		if arr[i] == nil {
			node = nil
		} else {
			node = &Node{Val: int(arr[i].(float64))}
		}
		if isLeft == 1 {
			currNode.Left = node
			nodes = append(nodes, currNode.Left)
		} else {
			currNode.Right = node
			nodes = append(nodes, currNode.Right)
			currNode = nodes[0]
			nodes = nodes[1:]
		}
		isLeft ^= 1
	}
	return root
}

func TreeNextToArray(root *Node) []interface{} {
	var ans []interface{}
	if root == nil {
		return ans
	}
	head := root
	for head != nil {
		var nxtHead *Node
		cur := head
		for cur != nil {
			if nxtHead == nil {
				if cur.Left != nil {
					nxtHead = cur.Left
				} else if cur.Right != nil {
					nxtHead = cur.Right
				}
			}
			ans = append(ans, cur.Val)
			cur = cur.Next
		}
		ans = append(ans, nil)
		head = nxtHead
	}
	return ans
}
