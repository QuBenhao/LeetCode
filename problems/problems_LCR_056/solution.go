package problemLCR_056

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
func findTarget(root *TreeNode, k int) bool {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var k int

	root = ArrayToTree(inputValues[0])
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return findTarget(root, k)
}
