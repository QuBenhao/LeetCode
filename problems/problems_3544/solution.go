package problem3544

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func subtreeInversionSum(edges [][]int, nums []int, k int) int64 {
	graph := map[int][]int{}
	for _, edge := range edges {
		a, b := edge[0], edge[1]
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}

	n := len(nums)

	memo := make([][][2]int64, n)
	for i := range memo {
		memo[i] = make([][2]int64, k)
		for j := range memo[i] {
			memo[i][j][0] = math.MinInt
			memo[i][j][1] = math.MinInt
		}
	}
	var dfs func(int, int, int, int) int64
	dfs = func(i, d, sign, pa int) int64 {
		if memo[i][d][max(sign, 0)] != math.MinInt {
			return memo[i][d][max(sign, 0)]
		}
		ans := int64(nums[i] * sign)
		if neighbours, ok := graph[i]; ok {
			// 能反转的话的结果
			cur := -int64(nums[i] * sign)
			for _, neigh := range neighbours {
				if neigh == pa {
					continue
				}
				// 不反转
				ans += dfs(neigh, max(0, d-1), sign, i)
				if d == 0 {
					// 能反转，传入k-1的距离（因为限制d==0代表可继续反转)
					cur += dfs(neigh, k-1, -sign, i)
				}
			}
			if d == 0 {
				// 能反转的话取最大
				ans = max(ans, cur)
			}
		} else if d == 0 {
			ans = max(ans, -ans)
		}
		memo[i][d][max(sign, 0)] = ans
		return ans
	}
	return dfs(0, 0, 1, -1)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return subtreeInversionSum(edges, nums, k)
}
