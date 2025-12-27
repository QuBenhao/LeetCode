package golang

import (
	"leetCode/problems/problems_Interview_08__04"
	"leetCode/problems/problems_Interview_16__06"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "Interview_16__06", "problems", problemInterview_16__06.Solve)
	TestEach(t, "Interview_08__04", "problems", problemInterview_08__04.Solve)
}
