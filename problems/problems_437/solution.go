package problem437

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
func pathSum(root *TreeNode, targetSum int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var targetSum int

	nodes := ArrayToTreeAndTargets(inputValues[0], )
	root,  = nodes[0], 
	if err := json.Unmarshal([]byte(inputValues[1]), &targetSum); err != nil {
		log.Fatal(err)
	}

	return pathSum(root, targetSum)
}
