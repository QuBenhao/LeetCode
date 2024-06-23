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

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var root *TreeNode

	root = ArrayToTree(values[0])

	return maxDepth(root)
}
