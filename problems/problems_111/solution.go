package problem111

import (
	. "leetCode/golang/models"
	"math"
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
func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	if root.Left == nil && root.Right == nil {
		return 1
	}
	ans := math.MaxInt32
	if root.Left != nil {
		ans = min(ans, minDepth(root.Left)+1)
	}
	if root.Right != nil {
		ans = min(ans, minDepth(root.Right)+1)
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var root *TreeNode

	root = ArrayToTree(values[0])

	return minDepth(root)
}
