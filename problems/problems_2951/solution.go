package problem2951

import (
	"encoding/json"
	"log"
	"strings"
)

func findPeaks(mountain []int) []int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var mountain []int

	if err := json.Unmarshal([]byte(values[0]), &mountain); err != nil {
		log.Fatal(err)
	}

	return findPeaks(mountain)
}
