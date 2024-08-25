package golang

import (
	"leetCode/problems/problems_240"
	"leetCode/problems/problems_LCR_042"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_042", "problems", problemLCR_042.Solve)
	TestEach(t, "240", "problems", problem240.Solve)
}
