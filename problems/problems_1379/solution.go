package problem1379

import (
	"encoding/json"
	. "leetCode/golang/models"
	"log"
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
func getTargetCopy(original, cloned, target *TreeNode) *TreeNode {
	if original == nil {
		return nil
	}
	if original == target {
		return cloned
	}
	left := getTargetCopy(original.Left, cloned.Left, target)
	if left != nil {
		return left
	}
	return getTargetCopy(original.Right, cloned.Right, target)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var original, cloned, target *TreeNode

	var targetVal int
	if err := json.Unmarshal([]byte(inputValues[1]), &targetVal); err != nil {
		log.Fatal(err)
	}
	nodes := ArrayToTreeAndTargets(inputValues[0], targetVal)
	original, target = nodes[0], nodes[1]
	cloned = ArrayToTree(inputValues[0])

	return TreeToArray(getTargetCopy(original, cloned, target))
}
