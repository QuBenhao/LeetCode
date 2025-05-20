package problem2710

import (
	"encoding/json"
	"log"
	"strings"
)

func removeTrailingZeros(num string) string {
	idx := len(num) - 1
	for ; idx >= 0 && num[idx] == '0'; idx-- {
	}
	return num[:idx+1]
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var num string

	if err := json.Unmarshal([]byte(values[0]), &num); err != nil {
		log.Fatal(err)
	}

	return removeTrailingZeros(num)
}
