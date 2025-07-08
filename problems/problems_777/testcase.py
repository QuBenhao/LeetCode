from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['RXXLRXRXL', 'XRLXXRRLX'], Output=True))
		self.testcases.append(case(Input=['X', 'L'], Output=False))
		self.testcases.append(case(Input=["RXXL","XLRX"], Output=False))
		self.testcases.append(case(Input=["RLX","XLR"], Output=False))
		self.testcases.append(case(Input=["RXR","XXR"], Output=False))
		self.testcases.append(case(Input=["RXR","XXR"], Output=False))

	def get_testcases(self):
		return self.testcases
