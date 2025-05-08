package problem2116

import (
	"encoding/json"
	"log"
	"strings"
)

func canBeValid(s string, locked string) bool {
	if len(s)%2 != 0 {
		return false
	}
	mn, mx := 0, 0
	for i, l := range locked {
		if l == 0 {
			mx++
			mn--
		} else {
			if s[i] == '(' {
				mx++
				mn++
			} else {
				mx--
				if mx < 0 {
					return false
				}
				mn--
			}
		}
		if mn < 0 {
			mn = 1
		}
	}
	return mn == 0
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var locked string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &locked); err != nil {
		log.Fatal(err)
	}

	return canBeValid(s, locked)
}
