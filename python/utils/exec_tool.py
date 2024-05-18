import os
import subprocess
from importlib.util import spec_from_file_location, module_from_spec


def check_problem_solved_python(dir_path, question_id: str, question_slug: str):
    testcase_spec = spec_from_file_location("module.name", f"{dir_path}/testcase.py")
    testcase = module_from_spec(testcase_spec)
    testcase_spec.loader.exec_module(testcase)
    testcase_obj = testcase.Testcase()
    solution_spec = spec_from_file_location("module.name", f"{dir_path}/solution.py")
    solution = module_from_spec(solution_spec)
    solution_spec.loader.exec_module(solution)
    solution_obj = solution.Solution()

    for test in testcase_obj.get_testcases():
        i, o = test
        result = solution_obj.solve(test_input=i)
        print("Question: [{}]{}, Input: {}, Output: {}, Expected: {}"
              .format(question_id, question_slug, i, result, o))
        if o is not None and result is None:
            raise ValueError("No solution")
        if o and isinstance(o, list):
            if o and isinstance(o, list) and isinstance(o[0], float):
                if any(abs(a - b) > 0.00001 for a, b in zip(o, result)):
                    raise ValueError("Mismatch float in list")
            elif all(x is not None for x in o) and isinstance(o[0], list) and not any(
                    None in x for x in o):
                if sorted(sorted(item) for item in o) != sorted(sorted(item) for item in result):
                    raise ValueError("List[List] not equal")
            else:
                if None not in o and not (isinstance(o[0], list) and any(None in x for x in o)):
                    if sorted(o) != sorted(result):
                        raise ValueError("List not equal")
                else:
                    if o != result:
                        raise ValueError("List Not equal")
        else:
            if isinstance(o, float):
                if abs(o - result) > 0.00001:
                    raise ValueError("Mismatch float")
            elif result != o:
                raise ValueError(f"Result {result} not as expected: {o}")


def check_problem_solved(language: str, root_path, dir_path, question_id: str, question_slug: str, func=None):
    match language:
        case "python3":
            file_name = "solution.py"
            lang_env = ["python", "--version"]
            test_commands = ["python", f"{root_path}/python/test.py"]
        case "java":
            file_name = "solution.java"
            lang_env = ["java", "--version"]
            test_commands = []
        case "cpp":
            file_name = "solution.cpp"
            lang_env = ["g++", "--version"]
            test_commands = []
        case "golang":
            file_name = "solution.go"
            lang_env = ["go", "version"]
            test_commands = [["go", "test", f"{root_path}/golang/solution_test.go"]]
        case "c":
            file_name = "solution.c"
            lang_env = ["gcc", "--version"]
            test_commands = []
        case "javascript":
            file_name = "solution.js"
            lang_env = ["npm", "test"]
            test_commands = []
        case "typescript":
            file_name = "solution.ts"
            lang_env = ["npm", "test"]
            test_commands = []
        case _:
            file_name = "unknown"
            lang_env = None
            test_commands = None
            print("Language {} is not implemented to save".format(language))

    if lang_env and test_commands and os.path.exists(f"{dir_path}/{file_name}"):
        env_check = subprocess.run(lang_env, capture_output=True, timeout=3)
        if env_check.returncode == 0:
            print("[{}] env ok, "
                  "output: {}".format(language,
                                      env_check.stdout.decode("utf-8")))
            for cmds in test_commands:
                execute_res = subprocess.run(cmds, capture_output=True, timeout=30)
                if execute_res.returncode != 0:
                    print("Execute failed, command: [{}],"
                          " error: {}, output: {}".format(" ".join(cmds),
                                                          execute_res.stderr.decode("utf-8"),
                                                          execute_res.stdout.decode("utf-8")))
                    return False
                print("Execute [{}] succeeded,"
                      " output: {}".format(" ".join(cmds),
                                           execute_res.stdout.decode("utf-8")))
            return True
        else:
            print("Execute language env [{}]\n"
                  "output: {}, err: {}".format(" ".join(lang_env),
                                               env_check.stdout.decode("utf-8"),
                                               env_check.stderr.decode("utf-8")))
    return False
