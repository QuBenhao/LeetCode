package problem2109

import (
	"encoding/json"
	"log"
	"strings"
)

func addSpaces(s string, spaces []int) string {
	var bytes []byte
	j, n := 0, len(spaces)
	for i := range s {
		if j < n && spaces[j] == i {
			bytes = append(bytes, ' ')
			j++
		}
		bytes = append(bytes, s[i])
	}
	return string(bytes)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var spaces []int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &spaces); err != nil {
		log.Fatal(err)
	}

	return addSpaces(s, spaces)
}
