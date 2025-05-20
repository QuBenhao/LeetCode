package problem815

import (
	"encoding/json"
	"log"
	"strings"
)

func numBusesToDestination(routes [][]int, source int, target int) int {
	if source == target {
		return 0
	}

	n := len(routes)
	edge := make([][]bool, n)
	for i := range edge {
		edge[i] = make([]bool, n)
	}

	rec := make(map[int][]int)
	for i, route := range routes {
		for _, site := range route {
			for _, j := range rec[site] {
				edge[i][j] = true
				edge[j][i] = true
			}
			rec[site] = append(rec[site], i)
		}
	}

	dis := make([]int, n)
	for i := range dis {
		dis[i] = -1
	}
	var q []int
	for _, site := range rec[source] {
		dis[site] = 1
		q = append(q, site)
	}
	for len(q) > 0 {
		x := q[0]
		q = q[1:]
		for y, b := range edge[x] {
			if b && dis[y] == -1 {
				dis[y] = dis[x] + 1
				q = append(q, y)
			}
		}
	}

	ret := 1 << 31
	for _, site := range rec[target] {
		if dis[site] != -1 && dis[site] < ret {
			ret = dis[site]
		}
	}
	if ret == 1<<31 {
		ret = -1
	}
	return ret
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var routes [][]int
	var source int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &routes); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &source); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &target); err != nil {
		log.Fatal(err)
	}

	return numBusesToDestination(routes, source, target)
}
