# [Rust] 递归 

> slug: rust-di-gui-by-himymben-dvfl
> date: 2024-08-21
> tags: Rust
> question: 二叉树剪枝 (pOCWxh)
> url: https://leetcode.cn/problems/pOCWxh/solutions/MlaGGi/rust-di-gui-by-himymben-dvfl/

---

> Problem: [LCR 047. 二叉树剪枝](https://leetcode.cn/problems/pOCWxh/description/)

# Code
```Rust []
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn prune_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
		if let Some(node) = root {
			let left = node.borrow_mut().left.take();
			let right = node.borrow_mut().right.take();
			node.borrow_mut().left = Self::prune_tree(left);
			node.borrow_mut().right = Self::prune_tree(right);
			if node.borrow().val == 0 && node.borrow().left.is_none() && node.borrow().right.is_none() {
				return None;
			}
			Some(node)
		} else {
			None
		}
    }
}
```
  
