from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcdf', 'dacbe'], Output=4))
		self.testcases.append(case(Input=['abceded', 'baecfef'], Output=4))
		self.testcases.append(case(Input=['abcdef', 'fedabc'], Output=2))
		self.testcases.append(case(Input=["abc","bca"], Output=2))
		self.testcases.append(case(Input=["boghiyx","kvjieak"], Output=7))

	def get_testcases(self):
		return self.testcases
