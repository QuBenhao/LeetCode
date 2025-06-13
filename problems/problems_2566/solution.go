package problem2566

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func minMaxDifference(num int) int {
	mx := num
	s := strconv.Itoa(num)
	for _, r := range s {
		if r != '9' {
			mx, _ = strconv.Atoi(strings.ReplaceAll(s, string(r), "9"))
			break
		}
	}
	mn, _ := strconv.Atoi(strings.ReplaceAll(s, s[:1], "0"))
	return mx - mn
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return minMaxDifference(num)
}
