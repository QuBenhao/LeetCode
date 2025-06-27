package problem1106

import (
	"encoding/json"
	"log"
	"strings"
)

func parseBoolExpr(expression string) bool {
	stack := [][]bool{{}}
	var operators []rune
	for _, c := range expression {
		switch c {
		case 't':
			stack[len(stack)-1] = append(stack[len(stack)-1], true)
		case 'f':
			stack[len(stack)-1] = append(stack[len(stack)-1], false)
		case '!', '&', '|':
			operators = append(operators, c)
		case '(':
			stack = append(stack, []bool{})
		case ')':
			op := operators[len(operators)-1]
			operators = operators[:len(operators)-1]
			arguments := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			var result bool
			switch op {
			case '!':
				result = !arguments[0]
			case '&':
				result = true
				for _, arg := range arguments {
					result = result && arg
					if !result {
						break
					}
				}
			case '|':
				result = false
				for _, arg := range arguments {
					result = result || arg
					if result {
						break
					}
				}
			}
			stack[len(stack)-1] = append(stack[len(stack)-1], result)
		case ',':
		default:
		}
	}
	return stack[0][0]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var expression string

	if err := json.Unmarshal([]byte(inputValues[0]), &expression); err != nil {
		log.Fatal(err)
	}

	return parseBoolExpr(expression)
}
