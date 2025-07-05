package problem1865

import (
	"encoding/json"
	"log"
	"strings"
)

type FindSumPairs struct {
	map1  map[int]int
	map2  map[int]int
	nums2 []int
}

func Constructor(nums1 []int, nums2 []int) FindSumPairs {
	map1 := make(map[int]int)
	map2 := make(map[int]int)
	for _, num := range nums1 {
		map1[num]++
	}
	for _, num := range nums2 {
		map2[num]++
	}
	return FindSumPairs{
		map1:  map1,
		map2:  map2,
		nums2: nums2,
	}
}

func (fsp *FindSumPairs) Add(index int, val int) {
	fsp.map2[fsp.nums2[index]]--
	fsp.nums2[index] += val
	fsp.map2[fsp.nums2[index]]++
}

func (fsp *FindSumPairs) Count(tot int) (count int) {
	for num1, freq1 := range fsp.map1 {
		count += fsp.map2[tot-num1] * freq1
	}
	return
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * obj := Constructor(nums1, nums2);
 * obj.Add(index,val);
 * param_2 := obj.Count(tot);
 */

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]any
	var ans []any
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	var nums1Arr []int
	if v, ok := opValues[0][0].([]int); ok {
		nums1Arr = v
	} else {
		for _, vi := range opValues[0][0].([]any) {
			nums1Arr = append(nums1Arr, int(vi.(float64)))
		}
	}
	var nums2Arr []int
	if v, ok := opValues[0][1].([]int); ok {
		nums2Arr = v
	} else {
		for _, vi := range opValues[0][1].([]any) {
			nums2Arr = append(nums2Arr, int(vi.(float64)))
		}
	}
	obj := Constructor(nums1Arr, nums2Arr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "add", "Add":
			res = nil
			obj.Add(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		case "count", "Count":
			res = obj.Count(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
