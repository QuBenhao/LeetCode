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

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var subRoot *TreeNode

	root = ArrayToTree(inputValues[0])
	subRoot = ArrayToTree(inputValues[1])

	return isSubtree(root, subRoot)
}
