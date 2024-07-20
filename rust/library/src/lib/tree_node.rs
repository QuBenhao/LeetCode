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

pub fn array_to_tree(arr: Vec<Option<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
    if arr.is_empty() {
        return None;
    }
    let mut root: Option<Rc<RefCell<TreeNode>>> = Some(Rc::new(RefCell::new(TreeNode::new(arr[0].unwrap()))));
    let mut is_left = true;
    let mut curr_nodes = VecDeque::new();
    let mut curr_node = &mut root;
    for i in 1..arr.len() {
        let num = arr[i];
        if is_left {
            if let Some(val) = num {
                let node = Rc::new(RefCell::new(TreeNode::new(val)));
                curr_node.as_mut().unwrap().borrow_mut().left = Some(node.clone());
                curr_nodes.push_back(node);
            }
        } else {
            if let Some(val) = num {
                let node = Rc::new(RefCell::new(TreeNode::new(val)));
                curr_node.as_mut().unwrap().borrow_mut().right = Some(node.clone());
                curr_nodes.push_back(node);
            }
            *curr_node = curr_nodes.pop_front();
        }
        is_left = !is_left;
    }
    root
}

pub fn tree_to_array(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Option<i32>> {
    let mut res = vec![];
    if root.is_none() {
        return res;
    }
    let mut nodes = VecDeque::new();
    nodes.push_back(root);
    while !nodes.is_empty() {
        let node = nodes.pop_front().unwrap();
        if let Some(n) = node {
            res.push(Some(n.borrow().val));
            nodes.push_back(n.borrow().left.clone());
            nodes.push_back(n.borrow().right.clone());
        } else {
            res.push(None);
        }
    }
    while let Some(None) = res.last() {
        res.pop();
    }
    res
}