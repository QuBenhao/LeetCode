package problem1306

import (
	"encoding/json"
	"log"
	"strings"
)

func canReach(arr []int, start int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int
	var start int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &start); err != nil {
		log.Fatal(err)
	}

	return canReach(arr, start)
}
