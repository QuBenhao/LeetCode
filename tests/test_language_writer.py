"""Unit tests for LanguageWriter type detection helpers."""

import pytest

from python.lc_libs.language_writer import (
    LanguageWriter,
    TREE_NODE_TYPES,
    LIST_NODE_TYPES,
    NODE_TYPES,
)


class TestTypeDetection:
    """Tests for type detection methods."""

    # ========== is_tree_node tests ==========

    @pytest.mark.parametrize("type_str", [
        "TreeNode",
        "*TreeNode",
        "TreeNode*",
        "TreeNode | null",
        "Option<Rc<RefCell<TreeNode>>>",
        "Option<Box<TreeNode>>",
        "List[TreeNode]",
        "[]*TreeNode",
        "vector<TreeNode*>",
        "TreeNode[]",
        "Array<TreeNode | null>",
    ])
    def test_is_tree_node_positive(self, type_str: str):
        """Test is_tree_node returns True for TreeNode types."""
        assert LanguageWriter.is_tree_node(type_str) is True

    @pytest.mark.parametrize("type_str", [
        "ListNode",
        "Node",
        "int",
        "string",
        "List[int]",
        "[]int",
        "",
        None,
    ])
    def test_is_tree_node_negative(self, type_str: str):
        """Test is_tree_node returns False for non-TreeNode types."""
        assert LanguageWriter.is_tree_node(type_str) is False

    # ========== is_list_node tests ==========

    @pytest.mark.parametrize("type_str", [
        "ListNode",
        "*ListNode",
        "ListNode*",
        "ListNode | null",
        "Option<Box<ListNode>>",
        "Option<Rc<RefCell<ListNode>>>",
        "List[ListNode]",
        "[]*ListNode",
        "vector<ListNode*>",
        "ListNode[]",
    ])
    def test_is_list_node_positive(self, type_str: str):
        """Test is_list_node returns True for ListNode types."""
        assert LanguageWriter.is_list_node(type_str) is True

    @pytest.mark.parametrize("type_str", [
        "TreeNode",
        "Node",
        "int",
        "",
        None,
    ])
    def test_is_list_node_negative(self, type_str: str):
        """Test is_list_node returns False for non-ListNode types."""
        assert LanguageWriter.is_list_node(type_str) is False

    # ========== is_node_type tests ==========

    @pytest.mark.parametrize("type_str", [
        "Node",
        "*Node",
        "Node | null",
        "_Node | null",
        "Option<Rc<RefCell<Node>>>",
    ])
    def test_is_node_type_positive(self, type_str: str):
        """Test is_node_type returns True for Node types."""
        assert LanguageWriter.is_node_type(type_str) is True

    @pytest.mark.parametrize("type_str", [
        "TreeNode",
        "ListNode",
        "int",
        "",
        None,
    ])
    def test_is_node_type_negative(self, type_str: str):
        """Test is_node_type returns False for non-Node types."""
        assert LanguageWriter.is_node_type(type_str) is False

    # ========== is_list_type tests ==========

    @pytest.mark.parametrize("type_str", [
        "[]int",
        "List[int]",
        "vector<int>",
        "Vec<int>",
        "Array<int>",
        "[]*TreeNode",
        "List[ListNode]",
    ])
    def test_is_list_type_positive(self, type_str: str):
        """Test is_list_type returns True for list types."""
        assert LanguageWriter.is_list_type(type_str) is True

    @pytest.mark.parametrize("type_str", [
        "int",
        "TreeNode",
        "ListNode",
        "",
        None,
    ])
    def test_is_list_type_negative(self, type_str: str):
        """Test is_list_type returns False for non-list types."""
        assert LanguageWriter.is_list_type(type_str) is False

    # ========== is_modify_in_place tests ==========

    def test_is_modify_in_place_positive(self):
        """Test detection of modify-in-place problems."""
        code = "Do not return anything, modify nums in-place instead."
        assert LanguageWriter.is_modify_in_place(code) is True

    def test_is_modify_in_place_negative(self):
        """Test detection of non-modify-in-place problems."""
        code = "Return the sorted array."
        assert LanguageWriter.is_modify_in_place(code) is False

    def test_is_modify_in_place_empty(self):
        """Test with empty code."""
        assert LanguageWriter.is_modify_in_place("") is False

    # ========== Testcase pattern detection ==========

    def test_is_cycle_linked_list_positive(self):
        """Test detection of cycle linked list testcases."""
        testcases = [
            [[1, 2, 3, 4], 1],
            [[5, 6], 0],
        ]
        assert LanguageWriter.is_cycle_linked_list(testcases, 1) is True

    def test_is_cycle_linked_list_wrong_param_count(self):
        """Test cycle detection with wrong param count."""
        testcases = [
            [[1, 2, 3, 4], 1],
        ]
        assert LanguageWriter.is_cycle_linked_list(testcases, 2) is False

    def test_is_cycle_linked_list_negative(self):
        """Test non-cycle testcases."""
        testcases = [
            [[1, 2, 3, 4], [5, 6]],  # Both lists
        ]
        assert LanguageWriter.is_cycle_linked_list(testcases, 1) is False

    def test_is_intersection_linked_list_positive(self):
        """Test detection of intersection linked list testcases."""
        testcases = [
            [8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3],
            [2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1],
        ]
        assert LanguageWriter.is_intersection_linked_list(testcases) is True

    def test_is_intersection_linked_list_negative(self):
        """Test non-intersection testcases."""
        testcases = [
            [[1, 2, 3], 4],  # Wrong format
        ]
        assert LanguageWriter.is_intersection_linked_list(testcases) is False

    def test_is_intersection_linked_list_empty(self):
        """Test with empty testcases."""
        assert LanguageWriter.is_intersection_linked_list(None) is False
        assert LanguageWriter.is_intersection_linked_list([]) is False

    # ========== Node subtype detection ==========

    def test_is_node_next_positive(self):
        """Test detection of Node with next pointer."""
        code = """
        class Node {
            int val;
            Node left;
            Node right;
            Node next;
        }
        """
        assert LanguageWriter.is_node_next(code) is True

    def test_is_node_next_negative_no_next(self):
        """Test Node without next pointer."""
        code = """
        class Node {
            int val;
            Node left;
            Node right;
        }
        """
        assert LanguageWriter.is_node_next(code) is False

    def test_is_node_neighbors_positive(self):
        """Test detection of Node with neighbors."""
        code = """
        class Node {
            int val;
            List<Node> neighbors;
        }
        """
        assert LanguageWriter.is_node_neighbors(code) is True

    def test_is_node_random_positive(self):
        """Test detection of Node with random pointer."""
        code = """
        class Node {
            int val;
            Node next;
            Node random;
        }
        """
        assert LanguageWriter.is_node_random(code) is True

    def test_is_node_random_negative_has_left_right(self):
        """Test Node with random but also left/right (should be NodeNext)."""
        code = """
        class Node {
            int val;
            Node left;
            Node right;
            Node next;
            Node random;
        }
        """
        assert LanguageWriter.is_node_random(code) is False  # Has left/right


class TestTypeConstants:
    """Tests for type detection constants."""

    def test_tree_node_types_not_empty(self):
        """Verify TREE_NODE_TYPES is not empty."""
        assert len(TREE_NODE_TYPES) > 0

    def test_list_node_types_not_empty(self):
        """Verify LIST_NODE_TYPES is not empty."""
        assert len(LIST_NODE_TYPES) > 0

    def test_tree_and_list_node_types_disjoint(self):
        """Verify TreeNode and ListNode types are distinct."""
        overlap = TREE_NODE_TYPES & LIST_NODE_TYPES
        # Only common element might be generic types like "Node"
        # But TreeNode and ListNode specific types should not overlap
        tree_specific = {t for t in TREE_NODE_TYPES if "TreeNode" in t}
        list_specific = {t for t in LIST_NODE_TYPES if "ListNode" in t}
        assert tree_specific & list_specific == set()

    def test_constants_are_immutable(self):
        """Verify type constants are frozenset (immutable)."""
        assert isinstance(TREE_NODE_TYPES, frozenset)
        assert isinstance(LIST_NODE_TYPES, frozenset)
        assert isinstance(NODE_TYPES, frozenset)