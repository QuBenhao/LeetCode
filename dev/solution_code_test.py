import sys

from lc_libs import write_solution

default_test_list = [
    "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:",

    "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         "
    "self.val = val\n#         self.next = next\nclass Solution:\n    def mergeKLists(self,"
    " lists: List[Optional[ListNode]]) -> Optional[ListNode]:",

    "class OrderedStream:\n\n    def __init__(self, n: int):\n\n\n    def insert(self, idKey: int, value: str) ->"
    " List[str]:\n\n\n\n# Your OrderedStream object will be instantiated and called as such:\n#"
    " obj = OrderedStream(n)\n# param_1 = obj.insert(idKey,value)",

    "class Bitset:\n\n    def __init__(self, size: int):\n\n\n    def fix(self, idx: int) -> None:\n\n\n    "
    "def unfix(self, idx: int) -> None:\n\n\n    def flip(self) -> None:\n\n\n    def all(self) -> bool:\n\n\n"
    "    def one(self) -> bool:\n\n\n    def count(self) -> int:\n\n\n    def toString(self) -> str:\n\n\n\n"
    "# Your Bitset object will be instantiated and called as such:\n# obj = Bitset(size)\n# obj.fix(idx)\n"
    "# obj.unfix(idx)\n# obj.flip()\n# param_4 = obj.all()\n# param_5 = obj.one()\n"
    "# param_6 = obj.count()\n# param_7 = obj.toString()",

    "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):"
    "\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass CBTInserter:\n\n"
    "    def __init__(self, root: Optional[TreeNode]):\n\n\n    def insert(self, val: int) -> int:\n\n\n"
    "    def get_root(self) -> Optional[TreeNode]:\n\n\n\n# Your CBTInserter object will be instantiated and"
    " called as such:\n# obj = CBTInserter(root)\n# param_1 = obj.insert(val)\n# param_2 = obj.get_root()",

    "# Definition for a binary tree node.\n# class TreeNode(object):\n#     def __init__(self, x):\n#         "
    "self.val = x\n#         self.left = None\n#         self.right = None\n\nclass Codec:\n\n    "
    "def serialize(self, root):\n        \"\"\"Encodes a tree to a single string.\n        \n        "
    ":type root: TreeNode\n        :rtype: str\n        \"\"\"\n        \n\n    def deserialize(self, data):\n"
    "        \"\"\"Decodes your encoded data to tree.\n        \n        :type data: str\n        :rtype: TreeNode\n"
    "        \"\"\"\n        \n\n# Your Codec object will be instantiated and called as such:\n"
    "# ser = Codec()\n# deser = Codec()\n# ans = deser.deserialize(ser.serialize(root))",

    "\"\"\"\n# Definition for a Node.\nclass Node:\n    def __init__(self, val = 0, neighbors = None):\n        "
    "self.val = val\n        self.neighbors = neighbors if neighbors is not None else []\n\"\"\"\n\n"
    "from typing import Optional\nclass Solution:\n    def cloneGraph(self, node: Optional['Node'])"
    " -> Optional['Node']:\n        ",

    "class FrequencyTracker:\n\n    def __init__(self):\n\n\n    def add(self, number: int) -> None:\n\n\n    "
    "def deleteOne(self, number: int) -> None:\n\n\n    def hasFrequency(self, frequency: int) -> bool:\n\n\n\n"
    "# Your FrequencyTracker object will be instantiated and called as such:\n# obj = FrequencyTracker()\n"
    "# obj.add(number)\n# obj.deleteOne(number)\n# param_3 = obj.hasFrequency(frequency)",

    "# Below is the interface for Iterator, which is already defined for you.\n#\n# class Iterator:\n"
    "#     def __init__(self, nums):\n#         \"\"\"\n#         Initializes an iterator object to the "
    "beginning of a list.\n#         :type nums: List[int]\n#         \"\"\"\n#\n#     def hasNext(self):\n#"
    "         \"\"\"\n#         Returns true if the iteration has more elements.\n#         :rtype: bool\n#         "
    "\"\"\"\n#\n#     def next(self):\n#         \"\"\"\n#         Returns the next element in the iteration.\n"
    "#         :rtype: int\n#         \"\"\"\n\nclass PeekingIterator:\n    def __init__(self, iterator):\n        "
    "\"\"\"\n        Initialize your data structure here.\n        :type iterator: Iterator\n        \"\"\"\n        "
    "\n\n    def peek(self):\n        \"\"\"\n        Returns the next element in the iteration without advancing the "
    "iterator.\n        :rtype: int\n        \"\"\"\n        \n\n    def next(self):\n        \"\"\"\n        "
    ":rtype: int\n        \"\"\"\n        \n\n    def hasNext(self):\n        \"\"\"\n        :rtype: bool\n        "
    "\"\"\"\n        \n\n# Your PeekingIterator object will be instantiated and called as such:\n"
    "# iter = PeekingIterator(Iterator(nums))\n# while iter.hasNext():\n#     val = iter.peek()   # Get the next "
    "element but not advance the iterator.\n#     iter.next()         # Should return the same value as [val]."
]


submit_test_list = [
    "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):"
    "\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    "
    "def countNodes(self, root: Optional[TreeNode]) -> int:\n        def depth(node):\n            h = 0\n            "
    "while node:\n                node = node.left\n                h += 1\n            return h\n\n        "
    "if not root:\n            return 0\n        left, right = depth(root.left), depth(root.right)\n        "
    "if left == right:\n            return self.countNodes(root.right) + (1 << right)\n        else:\n            "
    "return self.countNodes(root.left) + (1 << right)\n",

    "class Solution:\n    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:\n        "
    "m, n = len(obstacleGrid), len(obstacleGrid[0])\n        dp = [0] * n\n        dp[0] = 1\n        "
    "for i in range(m):\n            for j in range(n):\n                if obstacleGrid[i][j] == 1:\n              "
    "      dp[j] = -1\n                elif j > 0:\n                    dp[j] = dp[j - 1] if dp[j] == -1 else (dp[j]"
    " if dp[j - 1] == -1 else dp[j] + dp[j - 1])\n        return dp[-1] if dp[-1] > 0 else 0\n",

    "class Solution:\n    def change(self, amount: int, coins: List[int]) -> int:\n        dp = [0] * (amount + 1)\n"
    "        dp[0] = 1\n        for c in coins:\n            for i in range(c, amount + 1):\n                "
    "dp[i] += dp[i - c]\n        return dp[-1]\n",
]


if __name__ == '__main__':
    for idx, test in enumerate(default_test_list):
        res = write_solution(test)
        with open(f"tmp_default{idx}.py", "w") as f:
            f.writelines(res)
    for idx, test in enumerate(submit_test_list):
        res = write_solution(test, False)
        with open(f"tmp_submit{idx}.py", "w") as f:
            f.writelines(res)
    sys.exit()
