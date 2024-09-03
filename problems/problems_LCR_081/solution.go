package problemLCR_081

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func combinationSum(candidates []int, target int) (ans [][]int) {
	sort.Ints(candidates)
	var backtrack func(int, int, []int)
	backtrack = func(idx, target int, path []int) {
		if target == 0 {
			ans = append(ans, append([]int(nil), path...))
			return
		}
		for i := idx; i < len(candidates); i++ {
			if target < candidates[i] {
				break
			}
			path = append(path, candidates[i])
			backtrack(i, target-candidates[i], path)
			path = path[:len(path)-1]
		}
	}
	backtrack(0, target, []int{})
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
