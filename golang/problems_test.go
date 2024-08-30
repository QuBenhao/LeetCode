package golang

import (
	"leetCode/problems/problems_238"
	"leetCode/problems/problems_437"
	"leetCode/problems/problems_LCR_090"
	"leetCode/problems/problems_LCR_105"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_105", "problems", problemLCR_105.Solve)
	TestEach(t, "LCR_090", "problems", problemLCR_090.Solve)
	TestEach(t, "437", "problems", problem437.Solve)
	TestEach(t, "238", "problems", problem238.Solve)
}
