package test

import (
	. "leetCode/golang/models"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test(t *testing.T) {
	arr := []int{1, 2, 3, 4, 5}
	node := IntArrayToLinkedList(arr)
	i := 0
	for tmp := node; tmp != nil; tmp = tmp.Next {
		assert.Equal(t, arr[i], tmp.Val)
		i++
	}
	assert.Equal(t, arr, LinkedListToIntArray(node))
}

func TestListNode(t *testing.T) {
	arr := []int{1, 2, 3, 4, 5}
	node := IntArrayToLinkedList(arr)
	i := 0
	for tmp := node; tmp != nil; tmp = tmp.Next {
		assert.Equal(t, arr[i], tmp.Val)
		i++
	}
	assert.Equal(t, arr, LinkedListToIntArray(node))

	cycleNode := IntArrayToLinkedListCycle(arr, 2)
	assert.NotNil(t, cycleNode)
	assert.NotNil(t, cycleNode.Next)
	assert.NotNil(t, cycleNode.Next.Next)
	assert.Equal(t, cycleNode.Next.Next, cycleNode.Next.Next.Next.Next.Next)

	intersectNodes := IntArrayToLinkedListIntersection(arr, []int{6, 7, 4, 5}, 4, 3, 2)
	assert.NotNil(t, intersectNodes)
	assert.Len(t, intersectNodes, 2)
	assert.Equal(t, intersectNodes[0].Val, arr[0])
	assert.Equal(t, intersectNodes[1].Val, 6)
	assert.Equal(t, intersectNodes[0].Next.Next.Next, intersectNodes[1].Next.Next)
}
