package problem104

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
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return max(maxDepth(root.Left), maxDepth(root.Right)) + 1
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var root *TreeNode

	root = ArrayToTree(values[0])

	return maxDepth(root)
}
