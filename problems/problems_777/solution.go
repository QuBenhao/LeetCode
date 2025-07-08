package problem777

import (
	"encoding/json"
	"log"
	"strings"
)

func canTransform(start string, result string) bool {
	n := len(start)
	i, j := 0, 0
	for i < n || j < n {
		for i < n && start[i] == 'X' {
			i++
		}
		for j < n && result[j] == 'X' {
			j++
		}
		if i == n || j == n {
			return i == j
		}
		if start[i] != result[j] {
			return false
		}
		if start[i] == 'L' && i < j {
			return false
		}
		if start[i] == 'R' && i > j {
			return false
		}
		i++
		j++
	}
	return i == j
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var start string
	var result string

	if err := json.Unmarshal([]byte(inputValues[0]), &start); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &result); err != nil {
		log.Fatal(err)
	}

	return canTransform(start, result)
}
