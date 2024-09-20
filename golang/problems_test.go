package golang

import (
	"leetCode/problems/problems_LCR_076"
	"leetCode/problems/problems_LCR_095"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_076", "problems", problemLCR_076.Solve)
	TestEach(t, "LCR_095", "problems", problemLCR_095.Solve)
}
