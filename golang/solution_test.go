package golang

import (
	problem "leetCode/problems/problems_241"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "241", "problems", problem.Solve)
}
