package problem226

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
func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	tmpRight := invertTree(root.Left)
	root.Left = invertTree(root.Right)
	root.Right = tmpRight
	return root
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var root *TreeNode

	root = ArrayToTree(values[0])

	return TreeToArray(invertTree(root))
}
