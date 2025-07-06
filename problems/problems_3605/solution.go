package problem3605

import (
	"encoding/json"
	"log"
	"strings"
)

func minStable(nums []int, maxC int) int {
	n := len(nums)
	gs := make([][][]int, n)
	for i, num := range nums {
		if i > 0 {
			gs[i] = make([][]int, len(gs[i-1]))
			for j := range gs[i-1] {
				gs[i][j] = make([]int, len(gs[i-1][j]))
				copy(gs[i][j], gs[i-1][j])
			}
		}
		gs[i] = append(gs[i], []int{num, i})
		j := 0
		for _, p := range gs[i] {
			p[0] = gcd(p[0], num)
			if gs[i][j][0] != p[0] {
				j++
				gs[i][j] = p
			}
		}
		gs[i] = gs[i][:j+1]
	}

	check := func(k int) bool {
		count := 0
		if k == 0 {
			for _, num := range nums {
				if num != 1 {
					count++
					if count > maxC {
						return false
					}
				}
			}
		} else {
			for i := n - 1; i >= 0; {
				found := false
				for j := len(gs[i]) - 1; j >= 0; j-- {
					v, idx := gs[i][j][0], gs[i][j][1]
					if v != 1 && i-idx+1 > k {
						count++
						if count > maxC {
							return false
						}
						i = max(i-k, idx) - 1
						found = true
						break
					}
				}
				if !found {
					i--
				}
			}
		}
		return true
	}

	left, right := 0, n
	for left < right {
		mid := (left + right) / 2
		if check(mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}

func gcd(a, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var maxC int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &maxC); err != nil {
		log.Fatal(err)
	}

	return minStable(nums, maxC)
}
