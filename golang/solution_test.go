package golang

import (
	problem "leetCode/problems/problems_3010"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3010", "problems", problem.Solve)
}
