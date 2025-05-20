package problemLCR_082

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func combinationSum2(candidates []int, target int) (ans [][]int) {
	var dfs func(int, int, []int)
	dfs = func(start, remain int, path []int) {
		if remain == 0 {
			ans = append(ans, append([]int(nil), path...))
			return
		}
		if start == len(candidates) || remain < 0 {
			return
		}
		path = append(path, candidates[start])
		dfs(start+1, remain-candidates[start], path)
		path = path[:len(path)-1]
		for start+1 < len(candidates) && candidates[start+1] == candidates[start] {
			start++
		}
		dfs(start+1, remain, path)
	}
	sort.Ints(candidates)
	dfs(0, target, nil)
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var candidates []int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &candidates); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return combinationSum2(candidates, target)
}
