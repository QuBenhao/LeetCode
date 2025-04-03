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
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode

	root = ArrayToTree(inputValues[0])

	return TreeToArray(lcaDeepestLeaves(root))
}
