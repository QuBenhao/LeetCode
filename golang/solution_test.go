package golang

import (
	problem "leetCode/problems/problems_402"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "402", "problems", problem.Solve)
}
