package problemLCR_055

import (

)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type BSTIterator struct {

}


func Constructor(root *TreeNode) BSTIterator {

}


func (this *BSTIterator) Next() int {

}


func (this *BSTIterator) HasNext() bool {

}


/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
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
	obj := Constructor(InterfaceArrayToTree(opValues[0][0].([]interface{})))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "next", "Next":
			res = obj.Next()
		case "hasNext", "HasNext":
			res = obj.HasNext()
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
