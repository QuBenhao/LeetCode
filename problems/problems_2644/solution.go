package problem2644

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func maxDivScore(nums []int, divisors []int) (ans int) {
	slices.SortFunc(nums, func(a, b int) int { return b - a })
	dup := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			dup++
		}
	}
	slices.Sort(divisors)
	maxCnt := -1
	for _, d := range divisors {
		if (maxCnt-dup+1)*d > nums[0] {
			break
		}
		cnt := 0
		for _, x := range nums {
			if x < d {
				break
			}
			if x%d == 0 {
				cnt++
			}
		}
		if cnt > maxCnt {
			maxCnt, ans = cnt, d
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int
	var divisors []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &divisors); err != nil {
		log.Fatal(err)
	}

	return maxDivScore(nums, divisors)
}
