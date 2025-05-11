package golang

import (
	"leetCode/problems/problems_LCR_039"
	"leetCode/problems/problems_LCR_040"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_039", "problems", problemLCR_039.Solve)
	TestEach(t, "LCR_040", "problems", problemLCR_040.Solve)
}
