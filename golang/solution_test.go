package golang

import (
	problem "leetCode/problems/problems_1401"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1401", "problems", problem.Solve)
}
