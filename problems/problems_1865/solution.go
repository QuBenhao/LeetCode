package problem1865

import (
	"encoding/json"
	"log"
	"strings"
)

type FindSumPairs struct {
    
}


func Constructor(nums1 []int, nums2 []int) FindSumPairs {
    
}


func (this *FindSumPairs) Add(index int, val int)  {
    
}


func (this *FindSumPairs) Count(tot int) int {
    
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
