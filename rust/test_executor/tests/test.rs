const PROBLEM_FOLDER: &str = "problems";
const PROBLEM_ID: &str = "1387";

#[cfg(test)]
mod test {
	use solution_1387 as solution;
    use test_executor::run_test::run_test;

    use crate::{PROBLEM_FOLDER, PROBLEM_ID};

    #[test]
    fn test_solution() {
        run_test(PROBLEM_ID, PROBLEM_FOLDER, solution::solve);
    }
}
