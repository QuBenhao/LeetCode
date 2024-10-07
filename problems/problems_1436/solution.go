package problem1436

import (
	"encoding/json"
	"log"
	"strings"
)

func destCity(paths [][]string) string {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var paths [][]string

	if err := json.Unmarshal([]byte(inputValues[0]), &paths); err != nil {
		log.Fatal(err)
	}

	return destCity(paths)
}
