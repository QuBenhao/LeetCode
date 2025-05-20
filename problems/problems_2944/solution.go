package problem2944

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumCoins(prices []int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var prices []int

	if err := json.Unmarshal([]byte(inputValues[0]), &prices); err != nil {
		log.Fatal(err)
	}

	return minimumCoins(prices)
}
