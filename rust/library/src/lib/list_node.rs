// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val,
        }
    }
}

pub fn int_array_to_list_node(arr: &Vec<i32>) -> Option<Box<ListNode>> {
    let mut dummy = Some(Box::new(ListNode::new(0)));
    let mut p = dummy.as_mut().unwrap();
    for i in arr {
        p.next = Some(Box::new(ListNode::new(*i)));
        p = p.next.as_mut().unwrap();
    }
    dummy.unwrap().next
}

pub fn list_node_to_int_array(head: &Option<Box<ListNode>>) -> Vec<i32> {
    let mut res = vec![];
    let mut node = head.clone();
    while let Some(n) = node {
        res.push(n.val);
        node = n.next;
    }
    res
}