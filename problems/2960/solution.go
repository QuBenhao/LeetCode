package problem2960

import (
	"encoding/json"
	"log"
	"strings"
)

func Solve(input string) int {
	values := strings.Split(input, "\n")
	var batteryPercentages []int

	if err := json.Unmarshal([]byte(values[0]), &batteryPercentages); err != nil {
		log.Fatal(err)
	}

	return countTestedDevices(batteryPercentages)
}

func countTestedDevices(batteryPercentages []int) int {

}