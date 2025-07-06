package golang

import (
	"leetCode/problems/problems_3602"
	"leetCode/problems/problems_3603"
	"leetCode/problems/problems_3604"
	"leetCode/problems/problems_3605"
	"leetCode/problems/problems_3606"
	"leetCode/problems/problems_3607"
	"leetCode/problems/problems_3608"
	"leetCode/problems/problems_3609"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3602", "problems", problem3602.Solve)
	TestEach(t, "3603", "problems", problem3603.Solve)
	TestEach(t, "3604", "problems", problem3604.Solve)
	TestEach(t, "3605", "problems", problem3605.Solve)
	TestEach(t, "3606", "problems", problem3606.Solve)
	TestEach(t, "3607", "problems", problem3607.Solve)
	TestEach(t, "3608", "problems", problem3608.Solve)
	TestEach(t, "3609", "problems", problem3609.Solve)
}
