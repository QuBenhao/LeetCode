package golang

import (
	"leetCode/problems/problems_LCR_060"
	"leetCode/problems/problems_LCR_064"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_060", "problems", problemLCR_060.Solve)
	TestEach(t, "LCR_064", "problems", problemLCR_064.Solve)
}
