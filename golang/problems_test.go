package golang

import (
	"leetCode/problems/problems_295"
	"leetCode/problems/problems_LCR_021"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "295", "problems", problem295.Solve)
	TestEach(t, "LCR_021", "problems", problemLCR_021.Solve)
}
