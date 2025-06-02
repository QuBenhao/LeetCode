package problem135

import (
	"encoding/json"
	"log"
	"strings"
)

func candy(ratings []int) (ans int) {
    n := len(ratings)
    arr := make([]int, n)
    arr[0] = 1
    for i := 1; i < n; i++ {
        if ratings[i] > ratings[i - 1] {
            arr[i] = arr[i - 1] + 1
        } else {
            arr[i] = 1
        }
    }
    for i, s := n - 2, 1; i >= 0; i-- {
        if ratings[i] > ratings[i + 1] {
            s++
            arr[i] = max(arr[i], s)
        } else {
            s = 1
        }
    }
    for _, v := range arr {
        ans += v
    }
    return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var ratings []int

	if err := json.Unmarshal([]byte(inputValues[0]), &ratings); err != nil {
		log.Fatal(err)
	}

	return candy(ratings)
}
