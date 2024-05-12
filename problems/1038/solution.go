package problem1038

import (
	. "leetCode/golang/models"
	"strings"
)

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var root *TreeNode

	root = ArrayToTree(values[0])

	return TreeToArray(bstToGst(root))
}

var sum int

func inorder(node *TreeNode) {
	if node == nil {
		return
	}
	inorder(node.Right)
	sum += node.Val
	node.Val = sum
	inorder(node.Left)
}

func bstToGst(root *TreeNode) *TreeNode {
	sum = 0
	inorder(root)
	return root
}
