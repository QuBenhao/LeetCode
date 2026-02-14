package golang

import (
	problem "leetCode/problems/problems_67"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "67", "problems", problem.Solve)
}
