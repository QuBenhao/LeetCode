package problem368

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func largestDivisibleSubset(nums []int) (ans []int) {
	sort.Ints(nums)
	n := len(nums)
	// 定义 f[i] 为考虑前 i 个数字，且以第 i 个数为结尾的最长「整除子集」长度。
	f := make([]int, n)
	// 定义 g[i] 为记录 f[i] 是由哪个下标的状态转移而来，如果 f[i] = f[j] + 1, 则有 g[i] = j。
	g := make([]int, n)

	for i := 0; i < n; i++ {
		// 至少包含自身一个数，因此起始长度为 1，由自身转移而来
		l := 1
		prev := i
		for j := 0; j < i; j++ {
			if nums[i]%nums[j] == 0 {
				// 如果能接在更长的序列后面，则更新「最大长度」&「从何转移而来」
				if f[j]+1 > l {
					l = f[j] + 1
					prev = j
				}
			}
		}

		// 记录「最终长度」&「从何转移而来」
		f[i] = l
		g[i] = prev
	}

	// 遍历所有的 f[i]，取得「最大长度」和「对应下标」
	max := -1
	idx := -1
	for i := 0; i < n; i++ {
		if f[i] > max {
			idx = i
			max = f[i]
		}
	}

	// 使用 g[] 数组回溯出具体方案
	for len(ans) != max {
		ans = append(ans, nums[idx])
		idx = g[idx]
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	res := largestDivisibleSubset(nums)
	sort.Ints(res)
	return res
}
