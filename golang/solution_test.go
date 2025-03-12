package golang

import (
	problem "leetCode/problems/problems_3306"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3306", "problems", problem.Solve)
}
