package problem662

import (
	. "leetCode/golang/models"
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
type Pair struct {
	Index int
	Node  *TreeNode
}

func widthOfBinaryTree(root *TreeNode) (ans int) {
	if root == nil {
		return 0
	}
	q := []Pair{{0, root}}
	for len(q) > 0 {
		size := len(q)
		ans = max(ans, q[size-1].Index-q[0].Index+1)
		for range size {
			p := q[0]
			q = q[1:]
			if p.Node.Left != nil {
				q = append(q, Pair{p.Index * 2, p.Node.Left})
			}
			if p.Node.Right != nil {
				q = append(q, Pair{p.Index*2 + 1, p.Node.Right})
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode

	root = ArrayToTree(inputValues[0])

	return widthOfBinaryTree(root)
}
