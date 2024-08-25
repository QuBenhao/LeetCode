#![allow(non_snake_case)]
use serde_json::{json, Value};

use std::collections::HashMap;
use std::rc::Rc;
use std::cell::RefCell;

struct DoubleLinkedList {
	key: i32,
	value: i32,
	prev: Option<Rc<RefCell<DoubleLinkedList>>>,
	next: Option<Rc<RefCell<DoubleLinkedList>>>,
}

impl DoubleLinkedList {
	fn new(key: i32, value: i32) -> Rc<RefCell<Self>> {
		Rc::new(RefCell::new(DoubleLinkedList {
			key,
			value,
			prev: None,
			next: None,
		}))
	}
}


struct LRUCache {
	capacity: i32,
	cache: HashMap<i32, Rc<RefCell<DoubleLinkedList>>>,
	head: Rc<RefCell<DoubleLinkedList>>,
	tail: Rc<RefCell<DoubleLinkedList>>,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LRUCache {

    fn new(capacity: i32) -> Self {
		let head = DoubleLinkedList::new(-1, -1);
		let tail = DoubleLinkedList::new(-1, -1);
		head.borrow_mut().next = Some(tail.clone());
		tail.borrow_mut().prev = Some(head.clone());
		LRUCache {
			capacity,
			cache: HashMap::new(),
			head,
			tail,
		}
    }
    
    fn get(&mut self, key: i32) -> i32 {
		if let Some(node) = self.cache.get(&key) {
			let node = node.clone();
			let value = node.borrow().value;
			self.remove_node(node.clone());
			self.insert_node(node.clone());
			value
		} else {
			-1
		}
    }
    
    fn put(&mut self, key: i32, value: i32) {
		if let Some(node) = self.cache.get(&key) {
			let node = node.clone();
			node.clone().borrow_mut().value = value;
			self.remove_node(node.clone());
			self.insert_node(node.clone());
		} else {
			if self.cache.len() == self.capacity as usize {
				let last = self.tail.borrow().prev.clone().unwrap();
				self.cache.remove(&last.borrow().key);
				self.remove_node(last.clone());
			}
			let new_node = DoubleLinkedList::new(key, value);
			self.cache.insert(key, new_node.clone());
			self.insert_node(new_node);
		}
    }

	fn remove_node(&mut self, node: Rc<RefCell<DoubleLinkedList>>) {
		let mut prev = node.borrow_mut().prev.take();
		let mut next = node.borrow_mut().next.take();
		prev.as_mut().unwrap().borrow_mut().next = next.clone();
		next.as_mut().unwrap().borrow_mut().prev = prev.clone();
	}

	fn insert_node(&mut self, node: Rc<RefCell<DoubleLinkedList>>) {
		let prev = self.head.clone();
		let next = self.head.borrow().next.clone().unwrap();
		node.borrow_mut().prev = Some(prev.clone());
		node.borrow_mut().next = Some(next.clone());
		prev.borrow_mut().next = Some(node.clone());
		next.borrow_mut().prev = Some(node.clone());
	}
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */

#[cfg(feature = "solution_LCR_031")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let capacity_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = LRUCache::new(capacity_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"get" => {
				let key: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.get(key)));
			},
			"put" => {
				let key: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let value: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				obj.put(key, value);
				ans.push(None);
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
