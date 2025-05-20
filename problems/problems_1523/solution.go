package problem1523

import (
	"encoding/json"
	"log"
	"strings"
)

func countOdds(low int, high int) (ans int) {
	ans = (high - low) / 2
	if low&1 == 1 || high&1 == 1 {
		ans++
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var low int
	var high int

	if err := json.Unmarshal([]byte(values[0]), &low); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &high); err != nil {
		log.Fatal(err)
	}

	return countOdds(low, high)
}
