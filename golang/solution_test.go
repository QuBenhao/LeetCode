package golang

import (
	problem "leetCode/problems/problems_812"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "812", "problems", problem.Solve)
}
