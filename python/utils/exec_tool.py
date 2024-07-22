import os
import subprocess


def check_problem_solved_and_write(question_id: str,
                                   language: str,
                                   problem_folder: str,
                                   root_path,
                                   dir_path,
                                   solution_file: str,
                                   test_file_path: str,
                                   write: bool = False,
                                   func=None,
                                   arguments=(),
                                   test_func=None) -> bool:
    file_name = solution_file
    main_file = str(os.path.join(root_path, test_file_path)) if test_file_path else None
    match language:
        case "python3":
            lang_env = ["python", "--version"]
            test_commands = [["python", main_file]]
        case "golang":
            lang_env = ["go", "version"]
            test_commands = [["go", "test", main_file, str(os.path.join(root_path, "golang/test_basic.go"))]]
        case "java":
            lang_env = ["mvn", "-v"]
            test_commands = [["mvn", "test", "-Dtest=qubhjava.test.TestMain"]]
        case "cpp":
            lang_env = ["bazel", "version"]
            test_commands = [["bazel", "test", "--cxxopt=-std=c++20", "//cpp:solution_test"]]
        case "c":
            lang_env = ["gcc", "--version"]
            test_commands = []
        case "javascript":
            lang_env = ["npm", "--version"]
            test_commands = [["npm", "test"]]
        case "typescript":
            lang_env = ["npm", "--version"]
            test_commands = [["npm", "test", "--alwaysStrict", "--strictBindCallApply",
                              "--strictFunctionTypes", "--target ES202", "typescript/test.ts"]]
        case _:
            file_name = "unknown"
            lang_env = None
            test_commands = None
            main_file = None
            print("Language {} is not implemented to save".format(language))

    if lang_env and test_commands and main_file and os.path.exists(f"{dir_path}/{file_name}"):
        env_check = subprocess.run(lang_env, capture_output=True, timeout=60)
        if env_check.returncode == 0:
            print("[{}] env ok, "
                  "output: {}".format(language,
                                      env_check.stdout.decode("utf-8")))
            try:
                with open(main_file, "r", encoding="utf-8") as f:
                    backup_content = f.read()
                with open(main_file, "w", encoding="utf-8") as f:
                    f.write(test_func(backup_content, problem_folder, question_id))
                all_pass = True
                for cmds in test_commands:
                    try:
                        execute_res = subprocess.run(cmds, capture_output=True, timeout=300, cwd=root_path)
                        if execute_res.returncode == 0:
                            print("Execute [{}] succeeded,"
                                  " output: {}".format(" ".join(cmds),
                                                       execute_res.stdout.decode("utf-8")))
                            continue
                        print("Execute failed, command: [{}],"
                              " error: {}, output: {}".format(" ".join(cmds),
                                                              execute_res.stderr.decode("utf-8"),
                                                              execute_res.stdout.decode("utf-8")))
                    except subprocess.TimeoutExpired as _:
                        print("Execute timeout, command: [{}]".format(" ".join(cmds)))
                    all_pass = False
                    break
            finally:
                with open(main_file, "w", encoding="utf-8") as f:
                    f.write(backup_content)
            if all_pass:
                return True
        else:
            print("Execute language env [{}]\n"
                  "output: {}, err: {}".format(" ".join(lang_env),
                                               env_check.stdout.decode("utf-8"),
                                               env_check.stderr.decode("utf-8")))
    if not write or not func or not file_name:
        return False
    with open(f"{dir_path}/{file_name}", "w", encoding="utf-8") as f:
        content = func(*arguments)
        f.writelines(content)
    return False
