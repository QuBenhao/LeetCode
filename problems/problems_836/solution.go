package problem836

import (
	"encoding/json"
	"log"
	"strings"
)

func isRectangleOverlap(rec1 []int, rec2 []int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var rec1 []int
	var rec2 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &rec1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &rec2); err != nil {
		log.Fatal(err)
	}

	return isRectangleOverlap(rec1, rec2)
}
