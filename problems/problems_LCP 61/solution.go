package problemLCP 61

import (
	"encoding/json"
	"log"
	"strings"
)

func temperatureTrend(temperatureA []int, temperatureB []int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var temperatureA []int
	var temperatureB []int

	if err := json.Unmarshal([]byte(values[0]), &temperatureA); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &temperatureB); err != nil {
		log.Fatal(err)
	}

	return temperatureTrend(temperatureA, temperatureB)
}
