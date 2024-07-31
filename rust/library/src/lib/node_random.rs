use std::cell::RefCell;
use std::rc::Rc;
// Definition for a Node.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub next: Option<Rc<RefCell<Node>>>,
    pub random: Option<Rc<RefCell<Node>>>,
}

impl Node {
    #[inline]
    pub fn new(val: i32) -> Self {
        Node {
            val,
            next: None,
            random: None,
        }
    }
}

pub fn array_to_node_random(arr: &Vec<Vec<Option<i32>>>) -> Option<Rc<RefCell<Node>>> {
    if arr.is_empty() {
        return None;
    }
    let mut nodes: Vec<Rc<RefCell<Node>>> = vec![];
    for i in 0..arr.len() {
        nodes.push(Rc::new(RefCell::new(Node::new(arr[i][0].unwrap()))));
    }
    for i in 0..arr.len() {
        let random = arr[i][1];
        if random.is_some() {
            nodes[i].borrow_mut().random = Some(nodes[random.unwrap() as usize].clone());
        }
        if i + 1 < arr.len() {
            nodes[i].borrow_mut().next = Some(nodes[i + 1].clone());
        }
    }
    Some(nodes[0].clone())
}

fn node_idx(root: &Option<Rc<RefCell<Node>>>, node: &Option<Rc<RefCell<Node>>>) -> i32 {
    let mut idx = 0;
    let mut cur = root.clone();
    while cur.is_some() {
        if cur == *node {
            break;
        }
        idx += 1;
        cur = cur.unwrap().borrow().next.clone();
    }
    idx
}

pub fn node_random_to_array(root: &Option<Rc<RefCell<Node>>>) -> Vec<Vec<Option<i32>>> {
    let mut res = vec![];
    if root.is_none() {
        return res;
    }
    let mut head = root.clone();
    while head.is_some() {
        let mut cur = vec![Some(head.clone().unwrap().borrow().val), None];
        if head.clone().unwrap().borrow().random.is_some() {
            cur[1] = Some(node_idx(&root, &head.clone().unwrap().borrow().random));
        }
        res.push(cur);
        let next_head = head.unwrap().borrow().next.clone();
        head = next_head;
    }
    res
}