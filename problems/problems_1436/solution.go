package problem1436

import (
	"encoding/json"
	"log"
	"strings"
)

func destCity(paths [][]string) string {
	cities := make(map[string]bool)

	for _, path := range paths {
		cities[path[0]] = true
	}

	for _, path := range paths {
		if !cities[path[1]] {
			return path[1]
		}
	}

	return ""
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var paths [][]string

	if err := json.Unmarshal([]byte(inputValues[0]), &paths); err != nil {
		log.Fatal(err)
	}

	return destCity(paths)
}
