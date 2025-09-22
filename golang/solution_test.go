package golang

import (
	problem "leetCode/problems/problems_165"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "165", "problems", problem.Solve)
}
