package problem2412

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumMoney(transactions [][]int) int64 {
	totalLoss, mx := int64(0), int64(0)
	for _, transaction := range transactions {
		totalLoss += int64(max(0, transaction[0]-transaction[1]))
		mx = max(mx, int64(min(transaction[0], transaction[1])))
	}
	return totalLoss + mx
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var transactions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &transactions); err != nil {
		log.Fatal(err)
	}

	return minimumMoney(transactions)
}
