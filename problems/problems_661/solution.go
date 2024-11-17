package problem661

import (
	"encoding/json"
	"log"
	"strings"
)

func imageSmoother(img [][]int) [][]int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var img [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &img); err != nil {
		log.Fatal(err)
	}

	return imageSmoother(img)
}
