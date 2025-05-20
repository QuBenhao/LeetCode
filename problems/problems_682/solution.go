package problem682

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func calPoints(operations []string) (ans int) {
	var arr []int
	for _, op := range operations {
		n := len(arr)
		if op == "C" {
			ans -= arr[n-1]
			arr = arr[:n-1]
			continue
		}
		switch op {
		case "+":
			arr = append(arr, arr[n-1]+arr[n-2])
		case "D":
			arr = append(arr, arr[n-1]*2)
		default:
			if v, err := strconv.Atoi(op); err == nil {
				arr = append(arr, v)
			}
		}
		ans += arr[n]
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var operations []string

	if err := json.Unmarshal([]byte(values[0]), &operations); err != nil {
		log.Fatal(err)
	}

	return calPoints(operations)
}
