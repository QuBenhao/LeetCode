from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16], Output=['This    is    an', 'example  of text', 'justification.  ']))
		self.testcases.append(case(Input=[['What', 'must', 'be', 'acknowledgment', 'shall', 'be'], 16], Output=['What   must   be', 'acknowledgment  ', 'shall be        ']))
		self.testcases.append(case(Input=[['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain', 'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do'], 20], Output=['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']))

	def get_testcases(self):
		return self.testcases
