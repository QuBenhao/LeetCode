package problem3117

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minimumValueSum(nums, andValues []int) int {
	const inf = math.MaxInt / 2 // Divide by 2 to prevent overflow in +nums[i] below
	n, m := len(nums), len(andValues)
	type args struct{ i, j, and int }
	memo := map[args]int{}
	var dfs func(int, int, int) int
	dfs = func(i, j, and int) int {
		if n-i < m-j { // Not enough elements remain
			return inf
		}
		if j == m { // Split into m segments
			if i == n {
				return 0
			}
			return inf
		}
		and &= nums[i]
		p := args{i, j, and}
		if res, ok := memo[p]; ok { // Already computed
			return res
		}
		res := dfs(i+1, j, and)  // Do not split here
		if and == andValues[j] { // Split here; nums[i] is the last number in this segment
			res = min(res, dfs(i+1, j+1, -1)+nums[i])
		}
		memo[p] = res // Memoization
		return res
	}
	ans := dfs(0, 0, -1)
	if ans == inf {
		return -1
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var andValues []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &andValues); err != nil {
		log.Fatal(err)
	}

	return minimumValueSum(nums, andValues)
}
