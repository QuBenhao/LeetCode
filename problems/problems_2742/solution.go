package problem2742

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func paintWalls(cost, time []int) int {
	n := len(cost)
	f := make([]int, n+1)
	for i := 1; i <= n; i++ {
		f[i] = math.MaxInt / 2 // 防止加法溢出
	}
	for i, c := range cost {
		t := time[i] + 1 // 注意这里加一了
		for j := n; j > 0; j-- {
			f[j] = min(f[j], f[max(j-t, 0)]+c)
		}
	}
	return f[n]
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var cost []int
	var time []int

	if err := json.Unmarshal([]byte(values[0]), &cost); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &time); err != nil {
		log.Fatal(err)
	}

	return paintWalls(cost, time)
}
