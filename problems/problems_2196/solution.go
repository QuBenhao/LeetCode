package problem2196

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
func createBinaryTree(descriptions [][]int) *TreeNode {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var descriptions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &descriptions); err != nil {
		log.Fatal(err)
	}

	return TreeToArray(createBinaryTree(descriptions))
}
