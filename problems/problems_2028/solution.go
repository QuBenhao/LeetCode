package problem2028

import (
	"encoding/json"
	"log"
	"strings"
)

func missingRolls(rolls []int, mean int, n int) []int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var rolls []int
	var mean int
	var n int

	if err := json.Unmarshal([]byte(values[0]), &rolls); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &mean); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[2]), &n); err != nil {
		log.Fatal(err)
	}

	return missingRolls(rolls, mean, n)
}
