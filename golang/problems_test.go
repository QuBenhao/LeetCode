package golang

import (
	"leetCode/problems/problems_128"
	"leetCode/problems/problems_LCR_074"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_074", "problems", problemLCR_074.Solve)
	TestEach(t, "128", "problems", problem128.Solve)
}
