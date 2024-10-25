package problem3181

import (
	"encoding/json"
	"log"
	"strings"
)

func maxTotalReward(rewardValues []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var rewardValues []int

	if err := json.Unmarshal([]byte(inputValues[0]), &rewardValues); err != nil {
		log.Fatal(err)
	}

	return maxTotalReward(rewardValues)
}
