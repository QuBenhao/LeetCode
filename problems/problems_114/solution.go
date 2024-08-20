package problem114

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
func flatten(root *TreeNode) {
	if root == nil {
		return
	}
	flatten(root.Left)
	flatten(root.Right)
	left, right := root.Left, root.Right
	root.Left, root.Right = nil, left
	last := root
	for last.Right != nil {
		last = last.Right
	}
	last.Right = right
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode

	root = ArrayToTree(inputValues[0])

	flatten(root)
	return TreeToArray(root)
}
