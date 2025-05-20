package problem3356

import (
	"encoding/json"
	"log"
	"strings"
)

func minZeroArray(nums []int, queries [][]int) int {
	//// 二分+差分
	//n, m := len(nums), len(queries)
	//check := func(x int) bool {
	//	diff := make([]int, n+1)
	//	for i := range x {
	//		l, r, v := queries[i][0], queries[i][1], queries[i][2]
	//		diff[l] += v
	//		diff[r+1] -= v
	//	}
	//	s := 0
	//	for i, num := range nums {
	//		s += diff[i]
	//		if s < num {
	//			return false
	//		}
	//	}
	//	return true
	//}
	//left, right := 0, m+1
	//for left < right {
	//	mid := (left + right) / 2
	//	if check(mid) {
	//		right = mid
	//	} else {
	//		left = mid + 1
	//	}
	//}
	//if left == m+1 {
	//	return -1
	//}
	//return left

	// 差分+双指针
	n, m := len(nums), len(queries)
	diff := make([]int, n+1)
	k := 0
	cur := 0
	for i, num := range nums {
		cur += diff[i]
		for k < m && cur < num {
			l, r, v := queries[k][0], queries[k][1], queries[k][2]
			diff[l] += v
			diff[r+1] -= v
			if l <= i && i <= r {
				cur += v
			}
			k++
		}
		if cur < num {
			return -1
		}
	}
	return k
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return minZeroArray(nums, queries)
}
