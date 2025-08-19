package golang

import (
	problem "leetCode/problems/problems_828"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "828", "problems", problem.Solve)
}
