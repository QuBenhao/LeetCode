package problem39

import (
	"encoding/json"
	"log"
	"strings"
)

func combinationSum(candidates []int, target int) (ans [][]int) {
	var dfs func([]int, int, int)
	dfs = func(path []int, idx int, s int) {
		if s == 0 {
			ans = append(ans, append([]int(nil), path...))
			return
		}
		if idx == len(candidates) {
			return
		}
		if candidates[idx] <= s {
			path = append(path, candidates[idx])
			dfs(path, idx, s-candidates[idx])
			path = path[:len(path)-1]
		}
		dfs(path, idx+1, s)
	}

	dfs([]int{}, 0, target)
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var candidates []int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &candidates); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return combinationSum(candidates, target)
}
