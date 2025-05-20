package problem2094

import (
	"encoding/json"
	"log"
	"strings"
)

func findEvenNumbers(digits []int) (ans []int) {
	count := make([]int, 10)
	for _, d := range digits {
		count[d]++
	}

	var dfs func(pos int, num int)
	dfs = func(pos int, num int) {
		if pos == 3 {
			ans = append(ans, num)
			return
		}
		for d, c := range count {
			if c == 0 || (pos == 0 && d == 0) || (pos == 2 && d%2 != 0) {
				continue
			}
			count[d]--
			dfs(pos+1, num*10+d)
			count[d]++
		}
	}
	dfs(0, 0)
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var digits []int

	if err := json.Unmarshal([]byte(inputValues[0]), &digits); err != nil {
		log.Fatal(err)
	}

	return findEvenNumbers(digits)
}
