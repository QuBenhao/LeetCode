package problem90

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func subsetsWithDup(nums []int) (ans [][]int) {
	sort.Ints(nums)
	n := len(nums)
	path := []int{}

	var backtrack func(idx int)
	backtrack = func(idx int) {
		if idx == n {
			cp := make([]int, len(path))
			copy(cp, path)
			ans = append(ans, cp)
			return
		}
		path = append(path, nums[idx])
		backtrack(idx + 1)
		path = path[:len(path)-1]
		nxt := idx + 1
		for nxt < n && nums[nxt] == nums[idx] {
			nxt++
		}
		backtrack(nxt)
	}
	backtrack(0)
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return subsetsWithDup(nums)
}
