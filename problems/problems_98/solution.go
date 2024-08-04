package problem98

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
func isValidBST(root *TreeNode) bool {
	var dfs func(root *TreeNode, min, max int) bool
	dfs = func(root *TreeNode, min, max int) bool {
		if root == nil {
			return true
		}
		if root.Val <= min || root.Val >= max {
			return false
		}
		return dfs(root.Left, min, root.Val) && dfs(root.Right, root.Val, max)
	}
	return dfs(root, math.MinInt, math.MaxInt)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode

	root = ArrayToTree(inputValues[0])

	return isValidBST(root)
}
