package golang

import (
	problem "leetCode/problems/problems_231"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "231", "problems", problem.Solve)
}
