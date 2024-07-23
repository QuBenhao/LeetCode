#[cfg(test)]
mod test {
    use library::lib::{list_node, tree_node};

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
}