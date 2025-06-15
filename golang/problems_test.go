package golang

import (
	"leetCode/problems/problems_3582"
	"leetCode/problems/problems_3583"
	"leetCode/problems/problems_3584"
	"leetCode/problems/problems_3585"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3582", "problems", problem3582.Solve)
	TestEach(t, "3583", "problems", problem3583.Solve)
	TestEach(t, "3584", "problems", problem3584.Solve)
	TestEach(t, "3585", "problems", problem3585.Solve)
}
