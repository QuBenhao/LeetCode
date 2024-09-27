package golang

import (
	"leetCode/problems/problems_LCR_033"
	"leetCode/problems/problems_LCR_044"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_033", "problems", problemLCR_033.Solve)
	TestEach(t, "LCR_044", "problems", problemLCR_044.Solve)
}
