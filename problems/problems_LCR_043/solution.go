package problemLCR_043

import (
	"encoding/json"
	"log"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type CBTInserter struct {

}


func Constructor(root *TreeNode) CBTInserter {

}


func (this *CBTInserter) Insert(v int) int {

}


func (this *CBTInserter) Get_root() *TreeNode {

}


/**
 * Your CBTInserter object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Insert(v);
 * param_2 := obj.Get_root();
 */

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]interface{}
	var ans []interface{}
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor(opValues[0][0].(*TreeNode))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "insert", "Insert":
			res = obj.Insert(int(opValues[i][0].(float64)))
		case "get_root", "Get_root":
			res = obj.Get_root()
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
