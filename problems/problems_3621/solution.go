package problem3621

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

var depths []int

func init() {
	maxN := uint64(1e15)
	length := 64 - bits.LeadingZeros64(maxN)
	depths = make([]int, length+1)
	for i := 2; i <= length; i++ {
		j := i
		for j > 1 {
			depths[i]++
			j = bits.OnesCount64(uint64(j))
		}
	}
}

func popcountDepth(n int64, k int) (ans int64) {
	if k == 0 {
		return 1
	}
	length := 64 - bits.LeadingZeros64(uint64(n))
	cache := make([][][]int64, length+1)
	for i := range cache {
		cache[i] = make([][]int64, length+1)
		for j := range cache[i] {
			cache[i][j] = make([]int64, 2)
			cache[i][j][0] = -1 // not limit
			cache[i][j][1] = -1 // limit
		}
	}
	var dfs func(int, bool, int) int64
	dfs = func(pos int, isLimit bool, count int) (cur int64) {
		if count < 0 || length-pos < count {
			return 0
		}
		if pos == length {
			return 1
		}
		if cache[pos][count][boolToInt(isLimit)] != -1 {
			return cache[pos][count][boolToInt(isLimit)]
		}
		var maxD int
		if isLimit {
			maxD = int(n >> (length - pos - 1) & 1)
		} else {
			maxD = 1
		}
		for d := 0; d <= maxD; d++ {
			cur += dfs(pos+1, isLimit && d == maxD, count-d)
		}
		cache[pos][count][boolToInt(isLimit)] = cur
		return cur
	}

	for i := 2; i <= length; i++ {
		if depths[i]+1 == k {
			ans += dfs(0, true, i)
		}
	}
	if k == 1 {
		ans += dfs(0, true, 1) - 1
	}
	return
}

func boolToInt(b bool) int {
	if b {
		return 1
	}
	return 0
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int64
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return popcountDepth(n, k)
}
