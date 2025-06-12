package problem3574

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func maxGCDScore(nums []int, k int) (ans int64) {
	gcd := func(a, b int64) int64 {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	n := len(nums)
	for i := range n {
		var lb_min int64
		lb_min = math.MaxInt64
		used, g := 0, int64(0)
		for j := i; j >= 0; j-- {
			x := int64(nums[j])
			lb := x & -x
			if lb < lb_min {
				lb_min = lb
				used = 1
			} else if lb == lb_min {
				used += 1
			}
			g = gcd(g, x)
			newG := g
			if used <= k {
				newG *= 2
			}
			if t := newG * int64(i-j+1); t > ans {
				ans = t
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxGCDScore(nums, k)
}
