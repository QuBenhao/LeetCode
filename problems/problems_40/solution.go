package problem40

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func combinationSum2(candidates []int, target int) (ans [][]int) {
	sort.Ints(candidates)
	n := len(candidates)
	var backtrack func(idx int, remain int, path []int)
	backtrack = func(idx, remain int, path []int) {
		if remain < 0 {
			return
		}
		if remain == 0 {
			cp := make([]int, len(path))
			copy(cp, path)
			ans = append(ans, cp)
			return
		}
		if idx == n {
			return
		}
		path = append(path, candidates[idx])
		backtrack(idx+1, remain-candidates[idx], path)
		path = path[:len(path)-1]
		nxt := idx + 1
		for nxt < n && candidates[nxt] == candidates[nxt-1] {
			nxt++
		}
		backtrack(nxt, remain, path)
	}
	backtrack(0, target, make([]int, 0))
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
