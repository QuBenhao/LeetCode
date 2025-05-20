package problem3072

import (
	"encoding/json"
	"log"
	"slices"
	"sort"
	"strings"
)

type fenwick []int

// 把下标为 i 的元素增加 v
func (f fenwick) add(i, v int) {
	for ; i < len(f); i += i & -i {
		f[i] += v
	}
}

// 返回下标在 [1,i] 的元素之和
func (f fenwick) pre(i int) (res int) {
	for ; i > 0; i &= i - 1 {
		res += f[i]
	}
	return
}

func resultArray(nums []int) (ans []int) {
	sorted := slices.Clone(nums)
	slices.Sort(sorted)
	sorted = slices.Compact(sorted)
	m := len(sorted)

	a := nums[:1]
	b := []int{nums[1]}
	t := make(fenwick, m+1)
	t.add(m-sort.SearchInts(sorted, nums[0]), 1)
	t.add(m-sort.SearchInts(sorted, nums[1]), -1)
	for _, x := range nums[2:] {
		v := m - sort.SearchInts(sorted, x)
		d := t.pre(v - 1) // 转换成 < v 的元素个数之差
		if d > 0 || d == 0 && len(a) <= len(b) {
			a = append(a, x)
			t.add(v, 1)
		} else {
			b = append(b, x)
			t.add(v, -1)
		}
	}
	return append(a, b...)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return resultArray(nums)
}
