package problem135

import (
	"encoding/json"
	"log"
	"strings"
)

func candy(ratings []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var ratings []int

	if err := json.Unmarshal([]byte(inputValues[0]), &ratings); err != nil {
		log.Fatal(err)
	}

	return candy(ratings)
}
