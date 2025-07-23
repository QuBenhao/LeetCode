package problem640

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func solveEquation(equation string) string {
	k, b, sign, cur := 0, 0, 1, 0
	last := '+'
	for _, c := range equation {
		if '0' <= c && c <= '9' {
			cur = cur*10 + int(c-'0')
		} else {
			if c == 'x' {
				if last != '0' && cur == 0 {
					cur = 1
				}
				k += sign * cur
			} else {
				b += sign * cur
				if c == '=' {
					sign = 1
					k *= -1
					b *= -1
				} else if c == '+' {
					sign = 1
				} else if c == '-' {
					sign = -1
				}
			}
			cur = 0
		}
		last = c
	}
	b += sign * cur
	if k == 0 {
		if b == 0 {
			return "Infinite solutions"
		}
		return "No solution"
	}
	return "x=" + strconv.Itoa(-b/k)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var equation string

	if err := json.Unmarshal([]byte(inputValues[0]), &equation); err != nil {
		log.Fatal(err)
	}

	return solveEquation(equation)
}
