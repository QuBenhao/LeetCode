package golang

import (
	"leetCode/problems/problems_LCR_007"
	"leetCode/problems/problems_300"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_007", "problems", problemLCR_007.Solve)
	TestEach(t, "300", "problems", problem300.Solve)
}
