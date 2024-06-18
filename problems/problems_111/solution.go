package problem111

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
func minDepth(root *TreeNode) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var root *TreeNode

	root = ArrayToTree(values[0])

	return minDepth(root)
}
