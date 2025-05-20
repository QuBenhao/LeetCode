package problem347

import (
	"encoding/json"
	"log"
	"strings"
)

func topKFrequent(nums []int, k int) []int {
	cnt := map[int]int{}
	for _, v := range nums {
		cnt[v]++
	}
	keys := make([]int, 0, len(cnt))
	for k := range cnt {
		keys = append(keys, k)
	}
	m := len(keys)
	var qSort func(int, int) int
	qSort = func(l, r int) int {
		if l >= r {
			return l
		}
		i, j, x := l-1, r+1, cnt[keys[(l+r)>>1]]
		for i < j {
			for i++; cnt[keys[i]] < x; i++ {
			}
			for j--; cnt[keys[j]] > x; j-- {
			}
			if i < j {
				keys[i], keys[j] = keys[j], keys[i]
			}
		}
		if m-k <= j {
			return qSort(l, j)
		}
		return qSort(j+1, r)
	}
	return keys[qSort(0, m-1):]
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return topKFrequent(nums, k)
}
