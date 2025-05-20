package problemLCR_028

import (
	"encoding/json"
	. "leetCode/golang/double_linked_node_child"
	"log"
	"strings"
)

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Prev *Node
 *     Next *Node
 *     Child *Node
 * }
 */

func flatten(root *Node) *Node {
	var dfs func(*Node) *Node
	dfs = func(node *Node) *Node {
		if node == nil {
			return node
		}
		last := node
		for node != nil {
			if node.Child != nil {
				childLast := dfs(node.Child)
				childLast.Next = node.Next
				if node.Next != nil {
					node.Next.Prev = childLast
				}
				node.Next = node.Child
				node.Child.Prev = node
				node.Child = nil
				node = childLast
			}
			last = node
			node = node.Next
		}
		return last
	}
	dfs(root)
	return root
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *Node
	var arr0 []any
	if err := json.Unmarshal([]byte(inputValues[0]), &arr0); err != nil {
		log.Fatal(err)
	}
	root = IntArrayToDoubleLinkedNode(arr0)

	return DoubleLinkedNodeToIntArray(flatten(root))
}
