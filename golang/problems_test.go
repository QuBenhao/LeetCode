package golang

import (
	"leetCode/problems/problems_76"
	"leetCode/problems/problems_LCR_079"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_079", "problems", problemLCR_079.Solve)
	TestEach(t, "76", "problems", problem76.Solve)
}
