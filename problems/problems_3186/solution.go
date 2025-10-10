package problem3186

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func maximumTotalDamage(power []int) int64 {
	mp := map[int]int{}
	for _, p := range power {
		mp[p]++
	}
	var keys []int
	for k := range mp {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	n := len(mp)
	dp := make([]int64, n+1)
	j := 0
	for i, cur := range keys {
		for keys[j] < cur-2 {
			j++
		}
		dp[i+1] = max(dp[i], dp[j]+int64(cur)*int64(mp[cur]))
	}
	return dp[n]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var power []int

	if err := json.Unmarshal([]byte(inputValues[0]), &power); err != nil {
		log.Fatal(err)
	}

	return maximumTotalDamage(power)
}
