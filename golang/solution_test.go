package golang

import (
	problem "leetCode/problems/problems_977"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "977", "problems", problem.Solve)
}
