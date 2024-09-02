package golang

import (
	"leetCode/problems/problems_287"
	"leetCode/problems/problems_LCR_075"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_075", "problems", problemLCR_075.Solve)
	TestEach(t, "287", "problems", problem287.Solve)
}
