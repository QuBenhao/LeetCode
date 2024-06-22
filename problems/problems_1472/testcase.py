from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['BrowserHistory', 'visit', 'visit', 'visit', 'back', 'back', 'forward', 'visit', 'forward', 'back', 'back'], [['leetcode.com'], ['google.com'], ['facebook.com'], ['youtube.com'], [1], [1], [1], ['linkedin.com'], [2], [2], [7]]], Output=[None, None, None, None, 'facebook.com', 'google.com', 'facebook.com', None, 'linkedin.com', 'google.com', 'leetcode.com']))
		self.testcases.append(case(Input=[["BrowserHistory","visit","back","back","forward","forward","visit","visit","back"],[["zav.com"],["kni.com"],[7],[7],[5],[1],["pwrrbnw.com"],["mosohif.com"],[9]]], Output=[None,None,"zav.com","zav.com","kni.com","kni.com",None,None,"zav.com"]))

	def get_testcases(self):
		return self.testcases
