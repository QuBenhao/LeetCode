package problem572

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
func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	var dfs func(root *TreeNode, subRoot *TreeNode, mustMatch bool) bool
	dfs = func(root *TreeNode, subRoot *TreeNode, mustMatch bool) bool {
		if root == nil || subRoot == nil {
			return root == nil && subRoot == nil
		}
		if root.Val == subRoot.Val && dfs(root.Left, subRoot.Left, true) && dfs(root.Right, subRoot.Right, true) {
			return true
		}
		if mustMatch {
			return false
		}
		return dfs(root.Left, subRoot, false) || dfs(root.Right, subRoot, false)
	}
	return dfs(root, subRoot, false)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var subRoot *TreeNode

	root = ArrayToTree(inputValues[0])
	subRoot = ArrayToTree(inputValues[1])

	return isSubtree(root, subRoot)
}
