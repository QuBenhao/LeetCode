package problem3628

import (
	"encoding/json"
	"log"
	"strings"
)

func numOfSubsequences(s string) int64 {
	n := len(s)
	sufT := make([]int, n+1)
	sufC := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		sufT[i] = sufT[i+1]
		sufC[i] = sufC[i+1]
		if s[i] == 'T' {
			sufT[i]++
		} else if s[i] == 'C' {
			sufC[i] += sufT[i]
		}
	}
	var ans, maxAdd int64
	preL, preC := 0, 0
	for i, c := range s {
		if c == 'L' {
			preL++
			ans += int64(sufC[i])
		} else if c == 'C' {
			preC += preL
		}
		maxAdd = max(maxAdd, int64(preC), int64(sufC[i]), int64(preL)*int64(sufT[i]))
	}
	return ans + maxAdd
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return numOfSubsequences(s)
}
