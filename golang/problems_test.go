package golang

import (
	"leetCode/problems/problems_4"
	"leetCode/problems/problems_LCR_081"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_081", "problems", problemLCR_081.Solve)
	TestEach(t, "4", "problems", problem4.Solve)
}
