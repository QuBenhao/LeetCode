package problem3117

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minimumValueSum(nums, andValues []int) int {
	const inf = math.MaxInt / 2 // 除 2 防止下面 +nums[i] 溢出
	n, m := len(nums), len(andValues)
	type args struct{ i, j, and int }
	memo := map[args]int{}
	var dfs func(int, int, int) int
	dfs = func(i, j, and int) int {
		if n-i < m-j { // 剩余元素不足
			return inf
		}
		if j == m { // 分了 m 段
			if i == n {
				return 0
			}
			return inf
		}
		and &= nums[i]
		p := args{i, j, and}
		if res, ok := memo[p]; ok { // 之前计算过
			return res
		}
		res := dfs(i+1, j, and)  // 不划分
		if and == andValues[j] { // 划分，nums[i] 是这一段的最后一个数
			res = min(res, dfs(i+1, j+1, -1)+nums[i])
		}
		memo[p] = res // 记忆化
		return res
	}
	ans := dfs(0, 0, -1)
	if ans == inf {
		return -1
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
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
