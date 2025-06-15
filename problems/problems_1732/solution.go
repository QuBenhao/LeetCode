package problem1732

import (
	"encoding/json"
	"log"
	"strings"
)

func largestAltitude(gain []int) (ans int) {
	cur := 0
	for _, g := range gain {
		cur += g
		if cur > ans {
			ans = cur
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var gain []int

	if err := json.Unmarshal([]byte(inputValues[0]), &gain); err != nil {
		log.Fatal(err)
	}

	return largestAltitude(gain)
}
