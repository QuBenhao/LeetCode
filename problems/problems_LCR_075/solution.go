package problemLCR_075

import (
	"encoding/json"
	"log"
	"strings"
)

func relativeSortArray(arr1 []int, arr2 []int) (ans []int) {
	mx := 0
	for _, v := range arr1 {
		mx = max(mx, v)
	}
	cnt := make([]int, mx+1)
	for _, v := range arr1 {
		cnt[v]++
	}
	for _, v := range arr2 {
		for cnt[v] > 0 {
			ans = append(ans, v)
			cnt[v]--
		}
	}
	for i := 0; i <= mx; i++ {
		for cnt[i] > 0 {
			ans = append(ans, i)
			cnt[i]--
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr1 []int
	var arr2 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &arr2); err != nil {
		log.Fatal(err)
	}

	return relativeSortArray(arr1, arr2)
}
