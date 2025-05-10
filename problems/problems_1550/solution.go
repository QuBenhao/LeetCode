package problem1550

import (
	"encoding/json"
	"log"
	"strings"
)

func threeConsecutiveOdds(arr []int) bool {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return threeConsecutiveOdds(arr)
}
