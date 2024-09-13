package golang

import (
	"leetCode/problems/problems_LCR_023"
	"leetCode/problems/problems_LCR_050"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_023", "problems", problemLCR_023.Solve)
	TestEach(t, "LCR_050", "problems", problemLCR_050.Solve)
}
