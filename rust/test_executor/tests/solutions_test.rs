const PROBLEMS: [[&str; 2]; 1] = [["problems", "1957"]];

#[cfg(test)]
mod test {
	use test_executor::run_test::run_test;
	use crate::PROBLEMS;

	use solution_1957 as solution;

	#[test]
	fn test_solutions() {
		for (i, problem) in PROBLEMS.iter().enumerate() {
			let (folder, id) = (problem[0], problem[1]);
			println!("Testing problem {}", id);
			run_test(id, folder, match i {
				0 => solution::solve,
				_ => panic!("Unknown solution"),
			});
		}
	}
}
