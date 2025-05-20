package problem860

import (
	"encoding/json"
	"log"
	"strings"
)

func lemonadeChange(bills []int) bool {
	fives, tens := 0, 0
	for _, bill := range bills {
		if bill == 5 {
			fives++
		} else if bill == 10 {
			tens++
			fives--
		} else if tens > 0 {
			tens--
			fives--
		} else {
			fives -= 3
		}
		if fives < 0 {
			return false
		}
	}
	return true
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var bills []int

	if err := json.Unmarshal([]byte(values[0]), &bills); err != nil {
		log.Fatal(err)
	}

	return lemonadeChange(bills)
}
