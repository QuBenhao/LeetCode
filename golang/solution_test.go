package golang

import (
	problem "leetCode/problems/problems_3011"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3011", "problems", problem.Solve)
}
