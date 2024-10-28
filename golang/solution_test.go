package golang

import (
	problem "leetCode/problems/problems_684"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "684", "problems", problem.Solve)
}
