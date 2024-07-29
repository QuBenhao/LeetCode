use std::cell::RefCell;
use std::rc::Rc;
use std::collections::HashSet;

// Definition for a Node.
#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub neighbors: Vec<Rc<RefCell<Node>>>,
}

impl Node {
    #[inline]
    pub fn new(val: i32) -> Self {
        Node {
            val,
            neighbors: Vec::new(),
        }
    }
}

pub fn array_to_node_neighbors(arr: &Vec<Vec<i32>>) -> Option<Rc<RefCell<Node>>> {
    if arr.is_empty() {
        return None;
    }
    let mut nodes: Vec<Rc<RefCell<Node>>> = vec![];
    for i in 0..arr.len() {
        nodes.push(Rc::new(RefCell::new(Node::new(i as i32 + 1))));
    }
    for i in 0..arr.len() {
        let neighbors = &arr[i];
        for j in 0..neighbors.len() {
            nodes[i].borrow_mut().neighbors.push(nodes[neighbors[j] as usize - 1].clone());
        }
    }
    Some(nodes[0].clone())
}

fn dfs(node: &Option<Rc<RefCell<Node>>>, visited: &mut HashSet<i32>, res: &mut Vec<Vec<i32>>) {
    if node.is_none() {
        return;
    }
    let node = node.as_ref().unwrap();
    for _ in res.len()..node.borrow().val as usize {
        res.push(vec![]);
    }
    let node_val = node.borrow().val;
    for neighbor in node.borrow().neighbors.iter() {
        let val = neighbor.borrow().val;
        res[node_val as usize - 1].push(val);
        if visited.contains(&val) {
            continue;
        }
        visited.insert(val);
        dfs(&Some(neighbor.clone()), visited, res);
    }
}

pub fn node_neighbors_to_array(root: &Option<Rc<RefCell<Node>>>) -> Vec<Vec<i32>> {
    let mut res = vec![];
    if root.is_none() {
        return res;
    }
    let mut visited = HashSet::new();
    visited.insert(root.as_ref().unwrap().borrow().val);
    dfs(&root.clone(), &mut visited, &mut res);
    res
}