package problem632

import (
	"container/heap"
	"encoding/json"
	"log"
	"math"
	"strings"
)

func smallestRange(nums [][]int) []int {
	h := make(hp, len(nums))
	r := math.MinInt
	for i, arr := range nums {
		h[i] = tuple{arr[0], i, 0} // 把每个列表的第一个元素入堆
		r = max(r, arr[0])
	}
	heap.Init(&h)

	ansL, ansR := h[0].x, r            // 第一个合法区间的左右端点
	for h[0].j+1 < len(nums[h[0].i]) { // 堆顶列表有下一个元素
		x := nums[h[0].i][h[0].j+1] // 堆顶列表的下一个元素
		r = max(r, x)               // 更新合法区间的右端点
		h[0].x = x                  // 替换堆顶
		h[0].j++
		heap.Fix(&h, 0)
		l := h[0].x // 当前合法区间的左端点
		if r-l < ansR-ansL {
			ansL, ansR = l, r
		}
	}
	return []int{ansL, ansR}
}

type tuple struct{ x, i, j int }
type hp []tuple

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].x < h[j].x }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (hp) Push(any)             {} // 没用到，可以不写
func (hp) Pop() (_ any)         { return }

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return smallestRange(nums)
}
