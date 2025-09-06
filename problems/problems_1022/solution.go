package problem1022

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
func sumRootToLeaf(root *TreeNode) int {
	if root == nil {
		return 0
	}
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, cur int) int {
		cur <<= 1
		cur += node.Val
		if node.Left == nil && node.Right == nil {
			return cur
		}
		res := 0
		if node.Left != nil {
			res += dfs(node.Left, cur)
		}
		if node.Right != nil {
			res += dfs(node.Right, cur)
		}
		return res
	}
	return dfs(root, 0)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode

	root = ArrayToTree(inputValues[0])

	return sumRootToLeaf(root)
}
