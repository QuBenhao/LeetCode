package problemLCR_050

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
	counter := make(map[int]int)
	counter[0] = 1

	var dfs func(*TreeNode, map[int]int, int) int
	dfs = func(node *TreeNode, counter map[int]int, target int) int {
		if node == nil {
			return 0
		}
		ret := 0
		target += node.Val
		ret += counter[target-targetSum]
		counter[target]++
		ret += dfs(node.Left, counter, target)
		ret += dfs(node.Right, counter, target)
		counter[target]--
		return ret
	}
	return dfs(root, counter, 0)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var root *TreeNode
	var targetSum int

	root = ArrayToTree(inputValues[0])
	if err := json.Unmarshal([]byte(inputValues[1]), &targetSum); err != nil {
		log.Fatal(err)
	}

	return pathSum(root, targetSum)
}
