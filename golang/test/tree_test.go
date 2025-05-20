package test

import (
	"fmt"
	. "leetCode/golang/models"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTree(t *testing.T) {
	node := ArrayToTree("[1,null,2]")
	assert.NotNil(t, node)
	assert.Equal(t, 1, node.Val)
	assert.Nil(t, node.Left)
	assert.Equal(t, 2, node.Right.Val)
	node2 := ArrayToTree("[1, null, 2]")
	assert.Equal(t, node, node2)
}

func TestTreeTarget(t *testing.T) {
	nodes := ArrayToTreeAndTargets("[1,2,3,null,4,null,5]", 5)
	node, target := nodes[0], nodes[1]
	assert.NotNil(t, node)
	assert.NotNil(t, target)
	assert.Equal(t, node.Right.Right, target)
	assert.Equal(t, 2, node.Left.Val)
	assert.Equal(t, 3, node.Right.Val)
	assert.Nil(t, node.Left.Left)
	assert.Equal(t, 4, node.Left.Right.Val)
	assert.Nil(t, node.Right.Left)
	assert.Equal(t, 5, node.Right.Right.Val)
}

func arrToStr(arr []any) string {
	res := "["
	for i, n := 0, len(arr); i < n; i++ {
		if arr[i] == nil {
			res += "null"
		} else {
			res += fmt.Sprintf("%v", arr[i])
		}
		if i < n-1 {
			res += ","
		}
	}
	res += "]"
	return res
}

func TestTreeToArray(t *testing.T) {
	node := ArrayToTree("[1,null,2]")
	assert.Equal(t, "[1,null,2]", arrToStr(TreeToArray(node)))
	node = ArrayToTree("[1,2,3,null,4,null,5]")
	assert.Equal(t, "[1,2,3,null,4,null,5]", arrToStr(TreeToArray(node)))
}
