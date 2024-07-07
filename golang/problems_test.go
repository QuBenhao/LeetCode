package golang

import (
	"leetCode/problems/problems_62"
	"leetCode/problems/problems_35"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "62", "problems", problem62.Solve)
	TestEach(t, "35", "problems", problem35.Solve)
}
