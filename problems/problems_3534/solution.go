package problem3534

import (
	"encoding/json"
	"log"
	"math/bits"
	"slices"
	"strings"
)

func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []int {
	idxes := make([]int, n)
	for i := range n {
		idxes[i] = i
	}
	slices.SortFunc(idxes, func(i, j int) int {
		return nums[i] - nums[j]
	})
	mapping := make([]int, n)
	for i, idx := range idxes {
		mapping[idx] = i
	}

	m := bits.Len(uint(n)) // Number of bits needed to represent n
	pa := make([][]int, n)
	for i := range pa {
		pa[i] = make([]int, m)
	}

	left := 0
	for i, j := range idxes {
		for nums[j]-nums[idxes[left]] > maxDiff {
			left++
		}
		pa[i][0] = left
	}

	for j := 1; j < m; j++ {
		for i := 0; i < n; i++ {
			pa[i][j] = pa[pa[i][j-1]][j-1]
		}
	}

	ans := make([]int, len(queries))
	for i, q := range queries {
		l, r := q[0], q[1]
		if l == r {
			ans[i] = 0
			continue
		}
		l, r = mapping[l], mapping[r]
		if l > r {
			l, r = r, l
		}
		res := 0
		for k := m-1; k >= 0; k-- {
			if pa[r][k] > l {
				res |= 1 << k
				r = pa[r][k]
			}
		}
		if pa[r][0] > l {
			ans[i] = -1
		} else {
			ans[i] = res + 1
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var nums []int
	var maxDiff int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxDiff); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &queries); err != nil {
		log.Fatal(err)
	}

	return pathExistenceQueries(n, nums, maxDiff, queries)
}
