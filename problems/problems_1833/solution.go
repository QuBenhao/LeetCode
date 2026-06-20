package problem1833

import (
	"encoding/json"
	"log"
	"strings"
)

func maxIceCream(costs []int, coins int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var costs []int
	var coins int

	if err := json.Unmarshal([]byte(inputValues[0]), &costs); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &coins); err != nil {
		log.Fatal(err)
	}

	return maxIceCream(costs, coins)
}
