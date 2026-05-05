package problem1861

import (
	"encoding/json"
	"log"
	"strings"
)

func rotateTheBox(boxGrid [][]byte) [][]byte {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var boxGrid [][]byte

	var boxGridStr [][]string
	if err := json.Unmarshal([]byte(inputValues[0]), &boxGridStr); err != nil {
		log.Fatal(err)
	}
	boxGrid = make([][]byte, len(boxGridStr))
	for i := 0; i < len(boxGrid); i++ {
		boxGrid[i] = make([]byte, len(boxGridStr[i]))
		for j := 0; j < len(boxGrid[i]); j++ {
			boxGrid[i][j] = boxGridStr[i][j][0]
		}
	}

	return rotateTheBox(boxGrid)
}

func byteArrToStrArr(arr [][]byte) []string {
	ans := make([]string, len(arr))
	for i, b := range arr {
		ans[i] = string(b)
	}
	return ans
}
