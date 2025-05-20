package problem2028

import (
	"encoding/json"
	"log"
	"strings"
)

func missingRolls(rolls []int, mean int, n int) []int {
	remain := mean * (len(rolls) + n)
	for _, roll := range rolls {
		remain -= roll
	}
	if remain < n || remain > 6*n {
		return nil
	}
	avg, extra := remain/n, remain%n
	ans := make([]int, n)
	for i := 0; i < extra; i++ {
		ans[i] = avg + 1
	}
	for i := extra; i < n; i++ {
		ans[i] = avg
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var rolls []int
	var mean int
	var n int

	if err := json.Unmarshal([]byte(values[0]), &rolls); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &mean); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[2]), &n); err != nil {
		log.Fatal(err)
	}

	return missingRolls(rolls, mean, n)
}
