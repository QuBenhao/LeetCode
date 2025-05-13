package problemLCR_035

import (
	"encoding/json"
	"log"
	"strings"
)

func findMinDifference(timePoints []string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var timePoints []string

	if err := json.Unmarshal([]byte(inputValues[0]), &timePoints); err != nil {
		log.Fatal(err)
	}

	return findMinDifference(timePoints)
}
