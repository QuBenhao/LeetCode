package problem763

import (
	"encoding/json"
	"log"
	"strings"
)

func partitionLabels(s string) (ans []int) {
	mp := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		mp[s[i]] = i
	}
	start, end := 0, 0
	for i := 0; i < len(s); i++ {
		end = max(end, mp[s[i]])
		if i == end {
			ans = append(ans, end-start+1)
			start = end + 1
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return partitionLabels(s)
}
