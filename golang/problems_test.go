package golang

import (
	"leetCode/problems/problems_LCR_113"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_113", "problems", problemLCR_113.Solve)
}
