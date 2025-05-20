package problem78

import (
	"encoding/json"
	"log"
	"strings"
)

func subsets(nums []int) (ans [][]int) {
	var dfs func(arr []int, idx int)
	dfs = func(arr []int, idx int) {
		if idx == len(nums) {
			copyArray := make([]int, 0, len(arr))
			copyArray = append(copyArray, arr...)
			ans = append(ans, copyArray)
			return
		}
		dfs(arr, idx+1)
		arr = append(arr, nums[idx])
		dfs(arr, idx+1)
		arr = arr[:len(arr)-1]
	}
	dfs(make([]int, 0), 0)
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return subsets(nums)
}
