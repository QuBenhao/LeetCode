package problem1656

import (
	"encoding/json"
	"log"
	"strings"
)

type OrderedStream struct {
	data []string
	ptr  int
}

func Constructor(n int) OrderedStream {
	d := make([]string, n)
	return OrderedStream{d, 0}
}

func (this *OrderedStream) Insert(idKey int, value string) []string {
	idKey--
	this.data[idKey] = value
	if idKey > this.ptr {
		return nil
	}
	for ; this.ptr < len(this.data) && this.data[this.ptr] != ""; this.ptr++ {
	}
	return this.data[idKey:this.ptr]
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Insert(idKey,value);
 */

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var opts []string
	var vals [][]any
	var ans []any
	if err := json.Unmarshal([]byte(values[0]), &opts); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(values[1]), &vals); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor(int(vals[0][0].(float64)))
	ans = append(ans, nil)
	for i := 1; i < len(opts); i++ {
		var res any
		switch opts[i] {
		case "insert", "Insert":
			res = obj.Insert(int(vals[i][0].(float64)), vals[i][1].(string))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
