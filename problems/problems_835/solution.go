package problem835

import (
	"encoding/json"
	"log"
	"strings"
)

func largestOverlap(img1 [][]int, img2 [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var img1 [][]int
	var img2 [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &img1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &img2); err != nil {
		log.Fatal(err)
	}

	return largestOverlap(img1, img2)
}
