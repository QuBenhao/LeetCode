use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

// Definition for a Node.
#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub left: Option<Rc<RefCell<Node>>>, // left child
    pub right: Option<Rc<RefCell<Node>>>, // right child
    pub next: Option<Rc<RefCell<Node>>>, // next child
}

impl Node {
    #[inline]
    pub fn new(val: i32) -> Self {
        Node {
            val,
            left: None,
            right: None,
            next: None,
        }
    }
}

pub fn array_to_tree_next(arr: &Vec<Option<i32>>) -> Option<Rc<RefCell<Node>>> {
    if arr.is_empty() {
        return None;
    }
    let root: Option<Rc<RefCell<Node>>> = Some(Rc::new(RefCell::new(Node::new(arr[0].unwrap()))));
    let mut queue = VecDeque::new();
    let mut cur_node = root.clone();
    let mut is_left = true;
    for i in 1..arr.len() {
        let num = arr[i];
        if num.is_some() {
            let node = Rc::new(RefCell::new(Node::new(num.unwrap())));
            if is_left {
                cur_node.as_ref().unwrap().borrow_mut().left = Some(node.clone());
            } else {
                cur_node.as_ref().unwrap().borrow_mut().right = Some(node.clone());
            }
            queue.push_back(node.clone());
        }
        if !is_left {
            cur_node = queue.pop_front();
        }
        is_left = !is_left;
    }
    root
}

pub fn tree_next_to_array(root: &Option<Rc<RefCell<Node>>>) -> Vec<Option<i32>> {
    let mut res = vec![];
    if root.is_none() {
        return res;
    }
    let mut head = root.clone();
    while head.is_some() {
        let mut cur = head.clone();
        let mut next_head: Option<Rc<RefCell<Node>>> = None;
        while cur.is_some() {
            if next_head.is_none() {
                if cur.as_ref().unwrap().borrow().left.is_some() {
                    next_head = cur.as_ref().unwrap().borrow().left.clone();
                } else {
                    next_head = cur.as_ref().unwrap().borrow().right.clone();
                }
            }
            res.push(Some(cur.as_ref().unwrap().borrow().val));
            let next = cur.as_ref().unwrap().borrow().next.clone();
            cur = next;
        }
        res.push(None);
        head = next_head;
    }
    res
}