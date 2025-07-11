package golang

import (
	problem "leetCode/problems/problems_1900"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1900", "problems", problem.Solve)
}
