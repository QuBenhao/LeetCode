package golang

import (
	"leetCode/problems/problems_LCR_073"
	"leetCode/problems/problems_LCR_086"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_073", "problems", problemLCR_073.Solve)
	TestEach(t, "LCR_086", "problems", problemLCR_086.Solve)
}
