package golang

import (
	problem "leetCode/problems/problems_1970"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1970", "problems", problem.Solve)
}
