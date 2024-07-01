package golang

import (
	"leetCode/problems/problems_1"
	"leetCode/problems/problems_2"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "1", "problems", problem1.Solve)
	TestEach(t, "2", "problems", problem2.Solve)
}
