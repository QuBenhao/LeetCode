const PROBLEMS: [[&str; 2]; 3] = [["problems", "LCR_063"], ["problems", "84"], ["problems", "416"]];

#[cfg(test)]
mod test {
	use test_executor::run_test::run_test;
	use crate::PROBLEMS;

	use solution_LCR_063 as solution0;
	use solution_84 as solution1;
	use solution_416 as solution2;

	#[test]
	fn test_solutions() {
		for (i, problem) in PROBLEMS.iter().enumerate() {
			let (folder, id) = (problem[0], problem[1]);
			println!("Testing problem {}", id);
			run_test(id, folder, match i {
				0 => solution0::solve,
				1 => solution1::solve,
				2 => solution2::solve,
				_ => panic!("Unknown solution"),
			});
		}
	}
}
