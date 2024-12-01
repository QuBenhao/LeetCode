const PROBLEM_FOLDER: &str = "problems";
const PROBLEM_ID: &str = "52";

#[cfg(test)]
mod test {
	use solution_52 as solution;
    use test_executor::run_test::run_test;

    use crate::{PROBLEM_FOLDER, PROBLEM_ID};

    #[test]
    fn test_solution() {
        run_test(PROBLEM_ID, PROBLEM_FOLDER, solution::solve);
    }
}
