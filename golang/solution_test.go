package golang

import (
	problem "leetCode/problems/problems_401"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "401", "problems", problem.Solve)
}
