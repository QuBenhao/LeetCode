package golang

import (
	"leetCode/problems/problems_Interview_08__02"
	"leetCode/problems/problems_Interview_16__03"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "Interview_08__02", "problems", problemInterview_08__02.Solve)
	TestEach(t, "Interview_16__03", "problems", problemInterview_16__03.Solve)
}
