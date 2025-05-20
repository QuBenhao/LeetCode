package problem100

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
func isSameTree(p *TreeNode, q *TreeNode) bool {
	return (p == nil && q == nil) || (p != nil && q != nil && p.Val == q.Val && isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right))
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var p *TreeNode
	var q *TreeNode

	p = ArrayToTree(values[0])
	q = ArrayToTree(values[1])

	return isSameTree(p, q)
}
