package golang

import (
	problem "leetCode/problems/problems_1301"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1301", "problems", problem.Solve)
}
