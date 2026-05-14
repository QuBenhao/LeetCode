package golang

import (
	problem "leetCode/problems/problems_153"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "153", "problems", problem.Solve)
}
