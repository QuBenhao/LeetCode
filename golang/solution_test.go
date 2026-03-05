package golang

import (
	problem "leetCode/problems/problems_1784"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1784", "problems", problem.Solve)
}
