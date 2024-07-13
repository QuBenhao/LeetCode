package golang

import (
	"leetCode/problems/problems_53"
	"leetCode/problems/problems_101"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "53", "problems", problem53.Solve)
	TestEach(t, "101", "problems", problem101.Solve)
}
