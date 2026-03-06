package golang

import (
	problem "leetCode/problems/problems_1888"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1888", "problems", problem.Solve)
}
