package golang

import (
	"leetCode/problems/problems_LCR_061"
	"leetCode/problems/problems_LCR_066"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_061", "problems", problemLCR_061.Solve)
	TestEach(t, "LCR_066", "problems", problemLCR_066.Solve)
}
