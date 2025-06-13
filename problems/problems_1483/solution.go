package problem1483

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

type TreeAncestor struct {
	m  int
	pa [][]int
}

func Constructor(n int, parent []int) TreeAncestor {
	m := bits.Len(uint(n))
	pa := make([][]int, n) // pa[i][j] = the j-th ancestor of node i
	for i := range n {
		pa[i] = make([]int, m)
		pa[i][0] = parent[i]
	}
	for j := 1; j < m; j++ {
		for i := range n {
			if p := pa[i][j-1]; p != -1 {
				pa[i][j] = pa[p][j-1]
			} else {
				pa[i][j] = -1
			}
		}
	}
	return TreeAncestor{pa: pa}
}

func (ta *TreeAncestor) GetKthAncestor(node int, k int) int {
	for ; k > 0 && node != -1; k &= k - 1 {
		// bits.TrailingZeros == bits.Len(k&-k)-1
		node = ta.pa[node][bits.TrailingZeros(uint(k))]
	}
	return node
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * obj := Constructor(n, parent);
 * param_1 := obj.GetKthAncestor(node,k);
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
	var parentArr []int
	if v, ok := opValues[0][1].([]int); ok {
		parentArr = v
	} else {
		for _, vi := range opValues[0][1].([]any) {
			parentArr = append(parentArr, int(vi.(float64)))
		}
	}
	obj := Constructor(int(opValues[0][0].(float64)), parentArr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "getKthAncestor", "GetKthAncestor":
			res = obj.GetKthAncestor(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
