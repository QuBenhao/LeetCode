package problem2240

import (
	"encoding/json"
	"log"
	"strings"
)

func waysToBuyPensPencils(total int, cost1 int, cost2 int) (ans int64) {
	for total >= 0 {
		ans += int64(total/cost2 + 1)
		total -= cost1
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var total int
	var cost1 int
	var cost2 int

	if err := json.Unmarshal([]byte(inputValues[0]), &total); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &cost1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &cost2); err != nil {
		log.Fatal(err)
	}

	return waysToBuyPensPencils(total, cost1, cost2)
}
