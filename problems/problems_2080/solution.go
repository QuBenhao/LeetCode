package problem2080

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

type RangeFreqQuery struct {
	idxMap map[int][]int
}

func Constructor(arr []int) RangeFreqQuery {
	idxMap := map[int][]int{}
	for i, num := range arr {
		idxMap[num] = append(idxMap[num], i)
	}
	return RangeFreqQuery{idxMap}
}

func (rfq *RangeFreqQuery) Query(left int, right int, value int) int {
	// sort.SearchInts 相当于 python的bisect.bisect_left
	return sort.SearchInts(rfq.idxMap[value], right+1) - sort.SearchInts(rfq.idxMap[value], left)
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * obj := Constructor(arr);
 * param_1 := obj.Query(left,right,value);
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
	var arr []int
	if v, ok := opValues[0][0].([]int); ok {
		arr = v
	} else {
		for _, vi := range opValues[0][0].([]any) {
			arr = append(arr, int(vi.(float64)))
		}
	}
	obj := Constructor(arr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "query", "Query":
			res = obj.Query(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)), int(opValues[i][2].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
