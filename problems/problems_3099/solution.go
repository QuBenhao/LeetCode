package problem3099

import (
	"encoding/json"
	"log"
	"strings"
)

func sumOfTheDigitsOfHarshadNumber(x int) int {
	s := 0
	for num := x; num > 0; num /= 10 {
		s += num % 10
	}
	if x%s != 0 {
		return -1
	}
	return s
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &x); err != nil {
		log.Fatal(err)
	}

	return sumOfTheDigitsOfHarshadNumber(x)
}
