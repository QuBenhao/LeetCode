package problem3074

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumBoxes(apple []int, capacity []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var apple []int
	var capacity []int

	if err := json.Unmarshal([]byte(inputValues[0]), &apple); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &capacity); err != nil {
		log.Fatal(err)
	}

	return minimumBoxes(apple, capacity)
}
