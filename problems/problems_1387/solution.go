package problem1387

import (
	"cmp"
	"encoding/json"
	"log"
	"maps"
	"slices"
	"strings"
)

func getKth(lo int, hi int, k int) int {
	cache := map[int]int{}
	var power func(int) int
	power = func(v int) (ans int) {
		if v == 1 {
			return 0
		}
		if val, ok := cache[v]; ok {
			return val
		}
		if v%2 == 0 {
			ans = power(v/2) + 1
		} else {
			ans = power((3*v+1)/2) + 2
		}
		cache[v] = ans
		return
	}

	counter := map[int]int{}
	for i := lo; i <= hi; i++ {
		counter[i] = power(i)
	}
	sorted := slices.SortedFunc(maps.Keys(counter), func(a, b int) int {
		return cmp.Or(cmp.Compare(counter[a], counter[b]), cmp.Compare(a, b))
	})
	return sorted[k-1]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var lo int
	var hi int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &lo); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &hi); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return getKth(lo, hi, k)
}
