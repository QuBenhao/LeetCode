package golang

import (
	problem "leetCode/problems/problems_815"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "815", "problems", problem.Solve)
}
