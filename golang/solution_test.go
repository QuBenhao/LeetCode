package golang

import (
	problem "leetCode/problems/problems_864"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "864", "problems", problem.Solve)
}
