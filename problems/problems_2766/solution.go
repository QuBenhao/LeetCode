package problem2766

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func relocateMarbles(nums []int, moveFrom []int, moveTo []int) []int {
	s := map[int]interface{}{}
	for _, v := range nums {
		s[v] = nil
	}
	for i := 0; i < len(moveFrom); i++ {
		f, t := moveFrom[i], moveTo[i]
		delete(s, f)
		s[t] = nil
	}
	res := make([]int, 0, len(s))
	for k := range s {
		res = append(res, k)
	}
	sort.Ints(res)
	return res
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var moveFrom []int
	var moveTo []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &moveFrom); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &moveTo); err != nil {
		log.Fatal(err)
	}

	return relocateMarbles(nums, moveFrom, moveTo)
}
