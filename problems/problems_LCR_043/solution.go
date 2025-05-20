package problemLCR_043

import (
	"encoding/json"
	. "leetCode/golang/models"
	"log"
	"math/bits"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type CBTInserter struct {
	root *TreeNode
	n    int
}

func Constructor(root *TreeNode) CBTInserter {
	n := 0
	var q []*TreeNode
	if root != nil {
		q = append(q, root)
		for len(q) > 0 {
			node := q[0]
			q = q[1:]
			n++
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}
	}
	return CBTInserter{root: root, n: n}
}

func (c *CBTInserter) Insert(val int) int {
	c.n++
	child := &TreeNode{Val: val}
	node := c.root
	for i := bits.Len(uint(c.n)) - 2; i > 0; i-- {
		if c.n>>i&1 == 0 {
			node = node.Left
		} else {
			node = node.Right
		}
	}
	if c.n&1 == 0 {
		node.Left = child
	} else {
		node.Right = child
	}
	return node.Val
}

func (c *CBTInserter) Get_root() *TreeNode {
	return c.root
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Insert(v);
 * param_2 := obj.Get_root();
 */

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]any
	var ans []any
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor(InterfaceArrayToTree(opValues[0][0].([]any)))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "insert", "Insert":
			res = obj.Insert(int(opValues[i][0].(float64)))
		case "get_root", "Get_root":
			res = TreeToArray(obj.Get_root())
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
