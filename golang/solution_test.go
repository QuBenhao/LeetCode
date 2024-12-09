package golang

import (
	problem "leetCode/problems/problems_935"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "935", "problems", problem.Solve)
}
