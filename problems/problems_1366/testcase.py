from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['ABC', 'ACB', 'ABC', 'ACB', 'ACB'], Output="ACB"))
		self.testcases.append(case(Input=['WXYZ', 'XYZW'], Output="XWYZ"))
		self.testcases.append(case(Input=['ZMNAGUEDSJYLBOPHRQICWFXTVK'], Output="ZMNAGUEDSJYLBOPHRQICWFXTVK"))
		self.testcases.append(case(Input=["BCA","CAB","CBA","ABC","ACB","BAC"], Output="ABC"))

	def get_testcases(self):
		return self.testcases
