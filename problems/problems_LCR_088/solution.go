package problemLCR_088

import (
	"encoding/json"
	"log"
	"strings"
)

func minCostClimbingStairs(cost []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var cost []int

	if err := json.Unmarshal([]byte(inputValues[0]), &cost); err != nil {
		log.Fatal(err)
	}

	return minCostClimbingStairs(cost)
}
