package golang

import (
	problem "leetCode/problems/problems_779"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "779", "problems", problem.Solve)
}
