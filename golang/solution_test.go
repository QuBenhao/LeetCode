package golang

import (
	problem "leetCode/problems/problems_462"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "462", "problems", problem.Solve)
}
