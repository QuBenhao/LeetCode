package golang

import (
	"leetCode/problems/problems_LCR_110"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_110", "problems", problemLCR_110.Solve)
}
