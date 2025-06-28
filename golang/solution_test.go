package golang

import (
	problem "leetCode/problems/problems_213"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "213", "problems", problem.Solve)
}
