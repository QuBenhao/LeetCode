from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['lc', 'cl', 'gg'], Output=6))
		self.testcases.append(case(Input=['ab', 'ty', 'yt', 'lc', 'cl', 'ab'], Output=8))
		self.testcases.append(case(Input=['cc', 'll', 'xx'], Output=2))
		self.testcases.append(case(Input=["zb","bb","zy","bz","yb","yz","zz","zy","zb","zz","by","by","bb","bz","bz","yy","bz","zz","bz","yy","yz","yz","zz","zy","by","zy","bb","yz","yy","by","zy","yz","yy","by","zz","bb","yb","by","yy","zb","bb","yz","yb","zz","by","yb","zy","bb","yz","zb","zy","yy","bb","by","yb","yb","bb","bb"], Output=110))

	def get_testcases(self):
		return self.testcases
