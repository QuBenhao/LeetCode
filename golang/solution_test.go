package golang

import (
	problem "leetCode/problems/problems_1111"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1111", "problems", problem.Solve)
}
