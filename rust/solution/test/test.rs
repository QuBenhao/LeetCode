const PROBLEM_FOLDER: &str = "problems";
const PROBLEM_ID: &str = "2";

#[cfg(test)]
mod test {
    use solution;
    use std::env;
    use std::{sync::mpsc, thread, time::Duration};
    use serde_json::Value;
    use crate::{PROBLEM_FOLDER, PROBLEM_ID};

    fn panic_after<T, F>(d: Duration, f: F) -> T
    where
        T: Send + 'static,
        F: FnOnce() -> T,
        F: Send + 'static,
    {
        let (done_tx, done_rx) = mpsc::channel();
        let handle = thread::spawn(move || {
            let val = f();
            done_tx.send(()).expect("Unable to send completion signal");
            val
        });

        match done_rx.recv_timeout(d) {
            Ok(_) => handle.join().expect("Thread panicked"),
            Err(_) => panic!("Thread took too long"),
        }
    }

    #[test]
    fn test_solution() {
        let data_file_path = env::current_dir()
            .expect("Failed to get current directory")
            .join(PROBLEM_FOLDER)
            .join(PROBLEM_FOLDER.to_owned() + "_" + PROBLEM_ID)
            .join("testcase");
        if !data_file_path.exists() {
            panic!("TestCase file not found: {:?}", data_file_path);
        }
        let content: String = std::fs::read_to_string(data_file_path)
            .expect("Failed to read data file");
        let mut input_strings: String = String::new();
        let mut expected_outputs: String = String::new();
        content.lines().for_each(|line| {
            if input_strings.is_empty() {
                input_strings = line.to_string();
            } else {
                expected_outputs = line.to_string();
            }
        });
        let inputs: Vec<String> = serde_json::from_str(&input_strings)
            .expect("Unable to parse input strings");
        let expected_outputs: Vec<Value> = serde_json::from_str(&expected_outputs)
            .expect("Unable to parse expected outputs");
        panic_after(Duration::from_secs(10), move || {
            for i in 0..inputs.len() {
                let inputs_clone = inputs.clone();
                let expected_outputs_clone = expected_outputs.clone();
                panic_after(Duration::from_secs(3), move || {
                    let result = solution::solve(inputs_clone[i].to_string());
                    assert_eq!(result, expected_outputs_clone[i], "Test case {}: [{}]", i, inputs_clone[i].replace('\n', ", "));
                });
            }
        });
    }
}