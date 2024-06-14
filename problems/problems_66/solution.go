package problem66

import (
	"encoding/json"
	"log"
	"strings"
)

func plusOne(digits []int) []int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var digits []int

	if err := json.Unmarshal([]byte(values[0]), &digits); err != nil {
		log.Fatal(err)
	}

	return plusOne(digits)
}
