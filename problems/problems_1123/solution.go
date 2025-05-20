package problem1123

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
func lcaDeepestLeaves(root *TreeNode) *TreeNode {
	type pair struct {
		node  *TreeNode
		depth int
	}
	var dfs func(*TreeNode) pair
	dfs = func(node *TreeNode) pair {
		if node == nil {
			return pair{node, 0}
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		if left.depth == right.depth {
			return pair{node, left.depth + 1}
		}
		if left.depth < right.depth {
			return pair{right.node, right.depth + 1}
		}
		return pair{left.node, left.depth + 1}
	}
	return dfs(root).node
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode

	root = ArrayToTree(inputValues[0])

	return TreeToArray(lcaDeepestLeaves(root))
}
