package golang

import (
	"leetCode/problems/problems_79"
	"leetCode/problems/problems_25"
	"leetCode/problems/problems_LCR_059"
	"leetCode/problems/problems_LCR_062"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "79", "problems", problem79.Solve)
	TestEach(t, "25", "problems", problem25.Solve)
	TestEach(t, "LCR_059", "problems", problemLCR_059.Solve)
	TestEach(t, "LCR_062", "problems", problemLCR_062.Solve)
}
