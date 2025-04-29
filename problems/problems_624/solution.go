package problem624

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func maxDistance(arrays [][]int) (ans int) {
	maxVal, minVal := arrays[0][len(arrays[0])-1], arrays[0][0]
	for i := 1; i < len(arrays); i++ {
		minCur, maxCur := arrays[i][0], arrays[i][len(arrays[i])-1]
		ans = max(ans, int(math.Abs(float64(maxVal-minCur))), int(math.Abs(float64(maxCur-minVal))))
		maxVal = max(maxVal, maxCur)
		minVal = min(minVal, minCur)
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arrays [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &arrays); err != nil {
		log.Fatal(err)
	}

	return maxDistance(arrays)
}
