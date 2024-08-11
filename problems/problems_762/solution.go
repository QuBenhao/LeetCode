package problem762

import (
	"encoding/json"
	"log"
	"strings"
)

func countPrimeSetBits(left int, right int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var left int
	var right int

	if err := json.Unmarshal([]byte(inputValues[0]), &left); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &right); err != nil {
		log.Fatal(err)
	}

	return countPrimeSetBits(left, right)
}
