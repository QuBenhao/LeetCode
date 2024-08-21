use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub fn array_to_tree(arr: &Vec<Option<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
    if arr.is_empty() {
        return None;
    }
    let root: Option<Rc<RefCell<TreeNode>>> = Some(Rc::new(RefCell::new(TreeNode::new(arr[0]?))));
    if let Some(mut cur_node) = root.clone() {
        let mut queue = VecDeque::new();
        let mut is_left = true;
        for i in 1..arr.len() {
            let num = arr[i];
            if num.is_some() {
                let node = Rc::new(RefCell::new(TreeNode::new(num?)));
                if is_left {
                    cur_node.borrow_mut().left = Some(node.clone());
                } else {
                    cur_node.borrow_mut().right = Some(node.clone());
                }
                queue.push_back(node.clone());
            }
            if !is_left {
                if let Some(next) = queue.pop_front() {
                    cur_node = next;
                }
            }
            is_left = !is_left;
        }
    }
    root
}

pub fn array_to_tree_with_targets(arr: &Vec<Option<i32>>, targets: Vec<i32>) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
    let tree = array_to_tree(&arr);
    let mut result_nodes = vec![None; targets.len() + 1];

    let mut queue = VecDeque::new();
    if let Some(root) = &tree {
        queue.push_back(root.clone());
        result_nodes[0] = Some(root.clone());
    }

    while let Some(node_rc) = queue.pop_front() {
        let node = node_rc.borrow();
        for i in 0..targets.len() {
            if node.val == targets[i] {
                result_nodes[i + 1] = Some(node_rc.clone());
                break;
            }
        }
        if let Some(left) = &node.left {
            queue.push_back(left.clone());
        }
        if let Some(right) = &node.right {
            queue.push_back(right.clone());
        }
    }

    result_nodes
}

pub fn tree_to_array(root: &Option<Rc<RefCell<TreeNode>>>) -> Vec<Option<i32>> {
    let mut res = vec![];
    if root.is_none() {
        return res;
    }
    let mut queue = VecDeque::new();
    queue.push_back(root.clone());
    while !queue.is_empty() {
        if let Some(node) = queue.pop_front().unwrap() {
            res.push(Some(node.borrow().val));
            queue.push_back(node.borrow().left.clone());
            queue.push_back(node.borrow().right.clone());
        } else {
            res.push(None);
        }
    }
    while res.last().unwrap().is_none() {
        res.pop();
    }
    res
}