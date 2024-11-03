package golang

import (
	problem "leetCode/problems/problems_633"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "633", "problems", problem.Solve)
}
