package golang

import (
	problem3652 "leetCode/problems/problems_3652"
	problem3653 "leetCode/problems/problems_3653"
	problem3654 "leetCode/problems/problems_3654"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3652", "problems", problem3652.Solve)
	TestEach(t, "3653", "problems", problem3653.Solve)
	TestEach(t, "3654", "problems", problem3654.Solve)
}
