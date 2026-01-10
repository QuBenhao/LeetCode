package golang

import (
	problem "leetCode/problems/problems_712"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "712", "problems", problem.Solve)
}
