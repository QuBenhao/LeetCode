package golang

import (
	"leetCode/problems/problems_208"
	"leetCode/problems/problems_LCR_068"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_068", "problems", problemLCR_068.Solve)
	TestEach(t, "208", "problems", problem208.Solve)
}
