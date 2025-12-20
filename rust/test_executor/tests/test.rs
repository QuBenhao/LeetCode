const PROBLEMS: [[&str; 2]; 2] = [["problems", "Interview_02__01"], ["problems", "Interview_10__01"]];

#[cfg(test)]
mod test {
	use test_executor::run_test::run_test;
	use crate::PROBLEMS;

	use solution_Interview_02__01 as solution0;
	use solution_Interview_10__01 as solution1;

	#[test]
	fn test_solutions() {
		for (i, problem) in PROBLEMS.iter().enumerate() {
			let (folder, id) = (problem[0], problem[1]);
			println!("Testing problem {}", id);
			run_test(id, folder, match i {
				0 => solution0::solve,
				1 => solution1::solve,
				_ => panic!("Unknown solution"),
			});
		}
	}
}
