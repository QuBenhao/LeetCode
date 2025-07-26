package golang

import (
	problem "leetCode/problems/problems_623"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "623", "problems", problem.Solve)
}
