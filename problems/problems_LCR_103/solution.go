package problemLCR_103

import (
	"encoding/json"
	"log"
	"strings"
)

func coinChange(coins []int, amount int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var coins []int
	var amount int

	if err := json.Unmarshal([]byte(inputValues[0]), &coins); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &amount); err != nil {
		log.Fatal(err)
	}

	return coinChange(coins, amount)
}
