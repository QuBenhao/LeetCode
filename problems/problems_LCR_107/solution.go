package problemLCR_107

import (
	"encoding/json"
	"log"
	"strings"
)

func updateMatrix(mat [][]int) [][]int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var mat [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &mat); err != nil {
		log.Fatal(err)
	}

	return updateMatrix(mat)
}
