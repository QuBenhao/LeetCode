package problem2101

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumDetonation(bombs [][]int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var bombs [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &bombs); err != nil {
		log.Fatal(err)
	}

	return maximumDetonation(bombs)
}
