package problem2412

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumMoney(transactions [][]int) int64 {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var transactions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &transactions); err != nil {
		log.Fatal(err)
	}

	return minimumMoney(transactions)
}
