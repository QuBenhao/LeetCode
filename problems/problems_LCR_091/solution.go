package problemLCR_091

import (
	"encoding/json"
	"log"
	"strings"
)

func minCost(costs [][]int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var costs [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &costs); err != nil {
		log.Fatal(err)
	}

	return minCost(costs)
}
