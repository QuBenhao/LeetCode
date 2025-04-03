package golang

import (
	problem "leetCode/problems/problems_1123"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1123", "problems", problem.Solve)
}
