package problem1948

import (
	"encoding/json"
	"log"
	"strings"
)

func deleteDuplicateFolder(paths [][]string) [][]string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var paths [][]string

	if err := json.Unmarshal([]byte(inputValues[0]), &paths); err != nil {
		log.Fatal(err)
	}

	return deleteDuplicateFolder(paths)
}
