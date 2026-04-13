"""
Shared fixtures for LeetCode project tests.

This module provides common test fixtures and utilities used across test files.
"""

import json
import pytest
from pathlib import Path
from typing import Dict, List, Any, Generator


# Project root path
PROJECT_ROOT = Path(__file__).parent.parent


@pytest.fixture
def project_root() -> Path:
    """Return the project root directory."""
    return PROJECT_ROOT


@pytest.fixture
def question_snippets_path() -> Path:
    """Return the path to question code snippets JSON file."""
    return PROJECT_ROOT / "python" / "dev" / "question_code_snippets.json"


@pytest.fixture
def question_snippets(question_snippets_path: Path) -> Generator[List[Dict[str, Any]], None, None]:
    """Load and yield question code snippets from JSON file."""
    if not question_snippets_path.exists():
        pytest.skip("question_code_snippets.json not found")
    with question_snippets_path.open("r", encoding="utf-8") as f:
        yield json.load(f)


@pytest.fixture
def sample_tree_node_code() -> str:
    """Return sample code with TreeNode type."""
    return """
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {

    }
};
"""


@pytest.fixture
def sample_list_node_code() -> str:
    """Return sample code with ListNode type."""
    return """
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {

    }
};
"""


@pytest.fixture
def sample_modify_in_place_code() -> str:
    """Return sample code for modify-in-place problem."""
    return """
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \"\"\"
        Do not return anything, modify nums in-place instead.
        \"\"\"
"""


@pytest.fixture
def sample_object_problem_code() -> str:
    """Return sample code for object-oriented problem."""
    return """
class MinStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""


@pytest.fixture
def sample_testcases_cycle_linked_list() -> List[List]:
    """Return sample testcases for cycle linked list problem."""
    return [
        [[3, 2, 0, -4], 1],
        [[1, 2], 0],
        [[1], -1],
    ]


@pytest.fixture
def sample_testcases_intersection_linked_list() -> List[List]:
    """Return sample testcases for intersection linked list problem."""
    return [
        [8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3],
        [2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1],
        [0, [2, 6, 4], [1, 5], 3, 2],
    ]


@pytest.fixture
def supported_languages() -> List[str]:
    """Return list of supported languages for code generation."""
    return ["python3", "cpp", "java", "typescript", "golang", "rust"]


@pytest.fixture
def language_writer_map():
    """Return a dict mapping language names to their Writer classes."""
    from python import lc_libs

    writers = {}
    for lang in ["python3", "cpp", "java", "typescript", "golang", "rust"]:
        cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
        if cls:
            writers[lang] = cls
    return writers
