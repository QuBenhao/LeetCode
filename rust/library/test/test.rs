#[cfg(test)]
mod test {
    use library::lib::{list_node, node_next, tree_node};

    #[test]
    fn test_list_node() {
        let nums = vec![1, 2, 3, 4, 5];
        let head = list_node::int_array_to_list_node(&nums);
        let res = list_node::list_node_to_int_array(&head);
        assert_eq!(nums, res);
        println!("{:?}", head);
    }

    #[test]
    fn test_tree_node() {
        let nums = vec![Some(1), None, Some(2), Some(3), Some(4), Some(5)];
        let root = tree_node::array_to_tree(&nums);
        let res = tree_node::tree_to_array(&root);
        assert_eq!(nums, res);
        println!("{:?}", root);
    }

    #[test]
    fn test_tree_node_with_targets() {
        let nums = vec![Some(1), Some(2), Some(3), Some(4), Some(5)];
        let targets = vec![1, 2, 4];
        let nodes = tree_node::array_to_tree_with_targets(&nums, targets);
        assert_eq!(nodes[0], nodes[1]);
        assert_eq!(nodes[0].as_ref().unwrap().borrow().left, nodes[2]);
        assert_eq!(nodes[0].as_ref().unwrap().borrow().left
                       .as_ref().unwrap().borrow().left, nodes[3]);
    }

    #[test]
    fn test_tree_node_with_next() {
        let nums = vec![Some(1), Some(2), Some(3), Some(4), Some(5)];
        let root = node_next::array_to_tree_next(&nums);
        let root_left = root.as_ref().unwrap().borrow().left.clone();
        let root_right = root.as_ref().unwrap().borrow().right.clone();
        let root_left_left = root_left.as_ref().unwrap().borrow().left.clone();
        let root_left_right = root_left.as_ref().unwrap().borrow().right.clone();
        root_left.as_ref().unwrap().borrow_mut().next = root_right.clone();
        root_left_left.as_ref().unwrap().borrow_mut().next = root_left_right.clone();
        let res = node_next::tree_next_to_array(&root);
        assert_eq!(vec![Some(1), None, Some(2), Some(3), None, Some(4), Some(5), None], res);
        println!("{:?}", root);
    }
}