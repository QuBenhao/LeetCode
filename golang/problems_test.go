package golang

import (
	"leetCode/problems/problems_153"
	"leetCode/problems/problems_LCR_047"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "153", "problems", problem153.Solve)
	TestEach(t, "LCR_047", "problems", problemLCR_047.Solve)
}
