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
	var dfs func(*TreeNode, map[int]int, int) int
	dfs = func(node *TreeNode, counter map[int]int, currSum int) int {
		if node == nil {
			return 0
		}
		currSum += node.Val
		ans := counter[currSum-targetSum]
		counter[currSum]++
		ans += dfs(node.Left, counter, currSum) + dfs(node.Right, counter, currSum)
		counter[currSum]--
		return ans
	}

	return dfs(root, map[int]int{0: 1}, 0)
}


func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var targetSum int

	root = ArrayToTree(inputValues[0])
	if err := json.Unmarshal([]byte(inputValues[1]), &targetSum); err != nil {
		log.Fatal(err)
	}

	return pathSum(root, targetSum)
}
