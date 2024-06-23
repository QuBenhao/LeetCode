package problem156

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
func upsideDownBinaryTree(root *TreeNode) *TreeNode {
	var node, left, right *TreeNode
	left = root
	for left != nil {
		new_left, new_right := left.Left, left.Right
		left.Left = right
		left.Right = node
		node = left
		left = new_left
		right = new_right
	}
	return node
}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var root *TreeNode

	root = ArrayToTree(values[0])

	return TreeToArray(upsideDownBinaryTree(root))
}
