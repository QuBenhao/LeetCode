package problem2769

import (
	"encoding/json"
	"log"
	"strings"
)

func theMaximumAchievableX(num int, t int) int {
	return num + t<<1
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var num int
	var t int

	if err := json.Unmarshal([]byte(values[0]), &num); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &t); err != nil {
		log.Fatal(err)
	}

	return theMaximumAchievableX(num, t)
}
