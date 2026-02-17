package golang

import (
	problem "leetCode/problems/problems_693"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "693", "problems", problem.Solve)
}
