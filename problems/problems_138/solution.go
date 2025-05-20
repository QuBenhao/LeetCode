package problem138

import (
	"encoding/json"
	. "leetCode/golang/node_random"
	"log"
	"strings"
)

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}
	for node := head; node != nil; node = node.Next.Next {
		node.Next = &Node{Val: node.Val, Next: node.Next}
	}
	for node := head; node != nil; node = node.Next.Next {
		if node.Random != nil {
			node.Next.Random = node.Random.Next
		}
	}
	headNew := head.Next
	for node := head; node != nil; node = node.Next {
		nodeNew := node.Next
		node.Next = node.Next.Next
		if nodeNew.Next != nil {
			nodeNew.Next = nodeNew.Next.Next
		}
	}
	return headNew
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var head *Node

	var arr0 [][]any
	if err := json.Unmarshal([]byte(values[0]), &arr0); err != nil {
		log.Fatal(err)
	}
	head = IntRandomArrayToNodeArray(arr0)

	return NodeArrayToIntRandomArray(copyRandomList(head))
}
