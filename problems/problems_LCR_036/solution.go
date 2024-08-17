package problemLCR_036

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func evalRPN(tokens []string) int {
	var values []int
	for _, token := range tokens {
		if strings.Contains("+-*/", token) {
			last := values[len(values)-1]
			values = values[:len(values)-1]
			switch token {
			case "+":
				values[len(values)-1] += last
			case "-":
				values[len(values)-1] -= last
			case "*":
				values[len(values)-1] *= last
			case "/":
				values[len(values)-1] /= last
			}
		} else {
			if value, err := strconv.Atoi(token); err == nil {
				values = append(values, value)
			}
		}
	}
	return values[0]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var tokens []string

	if err := json.Unmarshal([]byte(inputValues[0]), &tokens); err != nil {
		log.Fatal(err)
	}

	return evalRPN(tokens)
}
