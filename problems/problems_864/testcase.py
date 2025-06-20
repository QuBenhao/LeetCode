from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['@.a..', '###.#', 'b.A.B'], Output=8))
		self.testcases.append(case(Input=['@..aA', '..B#.', '....b'], Output=6))
		self.testcases.append(case(Input=['@Aa'], Output=-1))

	def get_testcases(self):
		return self.testcases
