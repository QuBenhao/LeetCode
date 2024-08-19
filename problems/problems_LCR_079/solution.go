package problemLCR_079

import (
	"encoding/json"
	"log"
	"strings"
)

func subsets(nums []int) (ans [][]int) {
	n := len(nums)
	var backtrack func(int, []int)
	backtrack = func(idx int, path []int) {
		if idx == n {
			ans = append(ans, append([]int(nil), path...))
			return
		}
		backtrack(idx+1, path)
		path = append(path, nums[idx])
		backtrack(idx+1, path)
		path = path[:len(path)-1]
	}
	backtrack(0, []int{})
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return subsets(nums)
}
