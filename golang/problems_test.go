package golang

import (
	"leetCode/problems/problems_45"
	"leetCode/problems/problems_LCR_015"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_015", "problems", problemLCR_015.Solve)
	TestEach(t, "45", "problems", problem45.Solve)
}
