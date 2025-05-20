package problem2960

import (
	"encoding/json"
	"log"
	"strings"
)

func countTestedDevices(batteryPercentages []int) (ans int) {
	for _, b := range batteryPercentages {
		if b > ans {
			ans++
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var batteryPercentages []int

	if err := json.Unmarshal([]byte(values[0]), &batteryPercentages); err != nil {
		log.Fatal(err)
	}

	return countTestedDevices(batteryPercentages)
}
