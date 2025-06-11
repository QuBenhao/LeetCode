package problem3445

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func maxDifference(s string, k int) int {
	ans := math.MinInt
	for x := range 5 {
		for y := range 5 {
			if x == y {
				continue
			}
			curSum := make([]int, 5)
			prevSum := make([]int, 5)
			minS := [][]int{{math.MaxInt32, math.MaxInt32}, {math.MaxInt32, math.MaxInt32}}
			left := 0
			for right, char := range s {
				curSum[char-'0']++
				for right-left+1 >= k && curSum[x] > prevSum[x] && curSum[y] > prevSum[y] {
					p, q := prevSum[x]&1, prevSum[y]&1
					minS[p][q] = min(minS[p][q], prevSum[x]-prevSum[y])
					prevSum[s[left]-'0']++
					left++
				}
				if right+1 >= k {
					ans = max(ans, curSum[x]-curSum[y]-minS[curSum[x]&1^1][curSum[y]&1])
				}
			}
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxDifference(s, k)
}
