package problemLCR_035

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func findMinDifference(timePoints []string) (ans int) {
	timeToInt := func(t string) int {
		h := int(t[0]-'0')*10 + int(t[1]-'0')
		m := int(t[3]-'0')*10 + int(t[4]-'0')
		return h*60 + m
	}

	arr := make([]int, len(timePoints))
	for i, t := range timePoints {
		arr[i] = timeToInt(t)
	}
	sort.Ints(arr)
	ans = 1440 + arr[0] - arr[len(arr)-1]
	for i := 1; i < len(arr); i++ {
		ans = min(ans, arr[i]-arr[i-1])
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var timePoints []string

	if err := json.Unmarshal([]byte(inputValues[0]), &timePoints); err != nil {
		log.Fatal(err)
	}

	return findMinDifference(timePoints)
}
