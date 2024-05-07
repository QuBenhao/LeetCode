package test

import (
	"github.com/stretchr/testify/assert"
	. "leetCode/golang/models"
)
import (
	"testing"
)

func Test(t *testing.T) {
	arr := []int{1, 2, 3, 4, 5}
	node := IntArrayToLinkedList(arr)
	i := 0
	for tmp := node; tmp != nil; tmp = tmp.Next {
		assert.Equal(t, arr[i], tmp.Val)
		i++
	}
	assert.Equal(t, arr, node.LinkedListToIntArray())
}
