package problem2951

import (
	"encoding/json"
	"log"
	"strings"
)

func findPeaks(mountain []int) (ans []int) {
	for i := 1; i < len(mountain)-1; i++ {
		if mountain[i] > mountain[i-1] && mountain[i] > mountain[i+1] {
			ans = append(ans, i)
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var mountain []int

	if err := json.Unmarshal([]byte(values[0]), &mountain); err != nil {
		log.Fatal(err)
	}

	return findPeaks(mountain)
}
