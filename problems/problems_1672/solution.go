package problem1672

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumWealth(accounts [][]int) (ans int) {
	for _, account := range accounts {
		s := 0
		for _, a := range account {
			s += a
		}
		ans = max(ans, s)
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var accounts [][]int

	if err := json.Unmarshal([]byte(values[0]), &accounts); err != nil {
		log.Fatal(err)
	}

	return maximumWealth(accounts)
}
