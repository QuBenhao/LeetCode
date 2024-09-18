package problemLCR_038

import (
	"encoding/json"
	"log"
	"strings"
)

func dailyTemperatures(temperatures []int) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var temperatures []int

	if err := json.Unmarshal([]byte(inputValues[0]), &temperatures); err != nil {
		log.Fatal(err)
	}

	return dailyTemperatures(temperatures)
}
