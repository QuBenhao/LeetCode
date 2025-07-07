import logging
from collections import deque
from pathlib import Path
from typing import Tuple, List, Optional

from python.constants import (
    SOLUTION_TEMPLATE_GOLANG,
    SOLUTION_TEMPLATE_GOLANG_MODIFY_IN_PLACE,
    TESTCASE_TEMPLATE_GOLANG,
)
from python.lc_libs.language_writer import LanguageWriter


class GolangWriter(LanguageWriter):

    def __init__(self) -> None:
        super().__init__()
        self.solution_file = "solution.go"
        self.main_folder = "golang"
        self.test_file = "solution_test.go"
        self.tests_file = "problems_test.go"
        self.basic_package_file = "test_basic.go"
        self.lang_env_commands = [["go", "version"]]
        self.test_commands = [
            [
                "go",
                "test",
                str(Path(self.main_folder) / self.test_file),
                str(Path(self.main_folder) / self.basic_package_file),
            ]
        ]

    def change_test(self, root_path: Path, problem_folder: str, question_id: str):
        with (root_path / self.main_folder / self.test_file).open("w", encoding="utf-8") as f:
            f.write(
                TESTCASE_TEMPLATE_GOLANG.format(
                    f'problem "leetCode/{problem_folder}/{problem_folder}_{question_id}"',
                    "TestSolution",
                    f'TestEach(t, "{question_id}", "{problem_folder}", problem.Solve)',
                )
            )

    def change_tests(self, root_path: Path, problem_ids_folders: list):
        pifs = problem_ids_folders.copy()
        pifs.sort(key=lambda x: f"{x[1]}_{x[0]}")
        with (root_path / self.main_folder / self.tests_file).open("w", encoding="utf-8") as f:
            f.write(
                TESTCASE_TEMPLATE_GOLANG.format(
                    "\n\t".join(
                        f'"leetCode/{pf}/{pf}_{pid}"' for pid, pf in pifs
                    ),
                    "TestSolutions",
                    "\n\t".join(
                        f'TestEach(t, "{pid}", "{pf}", problem{pid}.Solve)'
                        for pid, pf in problem_ids_folders
                    ),
                )
            )

    def get_test_problem_id(self, root_path: Path, problem_folder: str) -> Optional[str]:
        """Get the problem ID from the test file."""
        test_file_path = root_path / self.main_folder / self.test_file
        with test_file_path.open("r", encoding="utf-8") as f:
            content = f.read()
        lines = content.split("\n")
        for line in lines:
            if (
                    'TestEach(t, "' in line
                    and f'", "{problem_folder}", problem.Solve)' in line
            ):
                return line.split('"')[1]
        return None

    def write_solution(
            self,
            code_default: str,
            code: str = None,
            problem_id: str = "",
            problem_folder: str = "",
    ) -> str:
        its = []
        rts = []
        func_names = []
        structs_map = dict()
        end_extra_code = ""
        testcases = LanguageWriter.get_test_cases(problem_folder, problem_id)
        for i, line in enumerate(code_default.split("\n")):
            line = line.strip()
            if line.startswith("func "):
                rts.append(line.split("{")[0].split(")")[-1].strip())
                its.append(
                    GolangWriter.__process_inputs(
                        code_default, line.split("(")[1].split(")")[0], structs_map, False, testcases,
                    )
                )
                func_names.append(line.split("(")[0].split("func ")[-1].strip())
            elif line.startswith("type ") and line.endswith(" struct {"):
                struct_name = line[len("type "): -len(" struct {")]
                structs_map[struct_name] = dict()
                for tmp in code_default.split("\n"):
                    tmp = tmp.strip()
                    if tmp.startswith("func ") and (
                            tmp.endswith(f") {struct_name} {{")
                            or tmp.endswith(f") *{struct_name} {{")
                    ):
                        tp0, tp1, tp2, tp3, tp4, tp5 = GolangWriter. __process_inputs(
                            code_default,
                            tmp.split("(")[1].split(")")[0],
                            structs_map,
                            True,
                            testcases,
                        )
                        rt = tmp.split("{")[0].split(")")[-1].strip()
                        structs_map[struct_name]["construct"] = (
                            tmp.split("(")[0].split("func ")[-1].strip(),
                            (tp0, tp1, tp2, tp3.replace("inputValues", "opValues[0]")),
                            tp4.replace("inputValues", "opValues[0]").replace("\t\t\t", "\t"),
                            rt,
                        )
                        end_extra_code += tp5
                    elif tmp.startswith("func (") and struct_name in tmp.split(")")[0]:
                        if "funcs" not in structs_map[struct_name]:
                            structs_map[struct_name]["funcs"] = []
                        tp0, tp1, tp2, tp3, tp4, tp5 = GolangWriter.__process_inputs(
                            code_default,
                            tmp.split("(")[2].split(")")[0],
                            structs_map,
                            True,
                            testcases,
                        )
                        rt = tmp.split("{")[0].split(")")[-1].strip()
                        structs_map[struct_name]["funcs"].append(
                            (
                                tmp.split("(")[1].split(")")[-1].strip(),
                                (
                                    tp0,
                                    tp1,
                                    tp2,
                                    tp3.replace("inputValues", "opValues[i]"),
                                    tp4.replace("inputValues", "opValues[i]"),
                                ),
                                rt,
                            )
                        )
                        end_extra_code += tp5

                import_set = set()
                func_loop = ""
                constructor = None
                for d in structs_map.values():
                    logging.debug("Struct: %s", d)
                    if "funcs" in d:
                        for name, its, rt in d["funcs"]:
                            logging.debug("Function: %s, its: %s, rt: %s", name, its, rt)
                            import_set.update(its[0])
                            if "TreeNode" in rt:
                                import_set.add('\t. "leetCode/golang/models"')
                                func_loop += (
                                    '\t\tcase "{}", "{}":\n' "\t\t\t{}{}TreeToArray(obj.{}({}))\n"
                                ).format(
                                    name[0].lower() + name[1:],
                                    name,
                                    its[4],
                                    "res = nil\n\t\t\t" if rt == "" else "res = ",
                                    name,
                                    its[3],
                                )
                            else:
                                func_loop += (
                                    '\t\tcase "{}", "{}":\n' "\t\t\t{}{}obj.{}({})\n"
                                ).format(
                                    name[0].lower() + name[1:],
                                    name,
                                    its[4],
                                    "res = nil\n\t\t\t" if rt == "" else "res = ",
                                    name,
                                    its[3],
                                )
                    if "construct" in d:
                        constructor = d["construct"]
                        import_set.update(constructor[1][0])
                build_body = (
                        "\tvar operators []string\n"
                        + "\tvar opValues [][]any\n"
                        + "\tvar ans []any\n"
                        + "\tif err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {\n"
                        + "\t\tlog.Println(err)\n"
                        + "\t\treturn nil\n"
                        + "\t}\n"
                        + "\tif err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {\n"
                        + "\t\tlog.Println(err)\n"
                        + "\t\treturn nil\n"
                        + "\t}\n"
                        + "{}".format(
                    (
                        f"\t{constructor[2]}obj := " + constructor[0] + f"({constructor[1][3]})\n"
                        if constructor is not None
                        else ""
                    ), "",
                )
                        + "\tans = append(ans, nil)\n"
                        + "\tfor i := 1; i < len(operators); i++ {\n"
                        + "\t\tvar res any\n"
                        + "{}".format("\t\tswitch operators[i] {\n" + func_loop + "\t\tdefault:\n"
                                                                                  "\t\t\tres = nil\n"
                                                                                  "\t\t}\n"
                                      )
                        + "\t\tans = append(ans, res)\n"
                          "\t}\n"
                )

                return SOLUTION_TEMPLATE_GOLANG.format(
                    problem_id,
                    "\n".join(
                        sorted(
                            import_set,
                            key=lambda x: (
                                "\t" + x.split(" ")[-1] if x.startswith("\t. ") else x
                            ),
                        )
                    ),
                    code or code_default,
                    build_body,
                    "",
                    "",
                    "ans",
                    "\n\n" + end_extra_code if end_extra_code else "",
                )
        import_set = set()
        for it in its:
            import_set.update(it[0])
            end_extra_code += it[5]

        if (
                len(rts) != 1
                or rts[0] == "*TreeNode"
                or rts[0] == "*ListNode"
                or rts[0] == "*Node"
        ):
            return_func_var = "{}({})".format(
                func_names[0], ", ".join(list(zip(*its))[3])
            )
            special_return_process = ""
            match rts[0]:
                case "*TreeNode":
                    import_set.add('\t. "leetCode/golang/models"')
                    return_line = f"TreeToArray({return_func_var})"
                case "*ListNode":
                    if "IntArrayToLinkedListCycle" in "".join(list(zip(*its))[2]):
                        logging.debug(return_func_var)
                        special_return_process = (f"res := {return_func_var}\n"
                                                  f"\tif res == nil {{\n"
                                                  f"\t\treturn nil\n"
                                                  f"\t}}\n\t")
                        return_line = "res.Val"
                    else:
                        import_set.add('\t. "leetCode/golang/models"')
                        return_line = f"LinkedListToIntArray({return_func_var})"
                case "*Node":
                    if (
                            "Left *Node" in code_default
                            and "Right *Node" in code_default
                            and "Next *Node" in code_default
                    ):
                        return_line = f"TreeNextToArray({return_func_var})"
                    elif "Neighbors []*Node" in code_default:
                        return_line = f"NodeNeighbourToArrayRelation({return_func_var})"
                    elif (
                            "/**\n"
                            " * Definition for a Node.\n"
                            " * type Node struct {\n"
                            " *     Val int\n"
                            " *     Next *Node\n"
                            " *     Random *Node\n"
                            " * }\n"
                            " */" in code_default
                    ):
                        return_line = f"NodeArrayToIntRandomArray({return_func_var})"
                    else:
                        return_line = f"FIXME({return_func_var})"
                case _:
                    return_line = return_func_var

            return SOLUTION_TEMPLATE_GOLANG.format(
                problem_id,
                # string with . starts before other, othercase sort normal
                "\n".join(
                    sorted(
                        import_set,
                        key=lambda x: (
                            "\t" + x.split(" ")[-1] if x.startswith("\t. ") else x
                        ),
                    )
                ),
                code or code_default,
                "\n".join(list(zip(*its))[1]),
                "\n".join(list(zip(*its))[2]),
                special_return_process,
                return_line,
                "\n\n" + end_extra_code if end_extra_code else "",
            )
        if rts[0] == "":
            logging.debug("Modify in place, its: %s", its)
            modify_in_place_return = its[0][3].split(",")[0].strip()
            if "TreeNode" in its[0][1]:
                modify_in_place_return = f"TreeToArray({modify_in_place_return})"
            elif "ListNode" in its[0][1]:
                modify_in_place_return = f"LinkedListToIntArray({modify_in_place_return})"
            elif "[]byte" in its[0][1]:
                modify_in_place_return = f"byteArrToStrArr({modify_in_place_return})"
            return SOLUTION_TEMPLATE_GOLANG_MODIFY_IN_PLACE.format(
                problem_id,
                "\n".join(
                    sorted(
                        import_set,
                        key=lambda x: (
                            "\t" + x.split(" ")[-1] if x.startswith("\t. ") else x
                        ),
                    )
                ),
                code_default if not code else code,
                "\n".join(list(zip(*its))[1]),
                "\n".join(list(zip(*its))[2]),
                func_names[0],
                ", ".join(list(zip(*its))[3]),
                modify_in_place_return,
                "\n\n" + end_extra_code if end_extra_code else "",
            )
        return SOLUTION_TEMPLATE_GOLANG.format(
            problem_id,
            "\n".join(
                sorted(
                    import_set,
                    key=lambda x: (
                        "\t" + x.split(" ")[-1] if x.startswith("\t. ") else x
                    ),
                )
            ),
            code or code_default,
            "\n".join(list(zip(*its))[1]),
            "\n".join(list(zip(*its))[2]),
            "",
            func_names[0] + "(" + ", ".join(list(zip(*its))[3]) + ")",
            "\n\n" + end_extra_code if end_extra_code else "",
        )

    def get_solution_code(
            self, root_path: Path, problem_folder: str, problem_id: str
    ) -> Tuple[str, str]:
        if not problem_id:
            with (root_path / self.main_folder / self.test_file).open("r", encoding="utf-8") as f:
                lines = f.read().split("\n")
                for line in lines:
                    if (
                            'TestEach(t, "' in line
                            and '", "problems", problem.Solve)' in line
                    ):
                        problem_id = line.split('"')[1]
                        break
        if not problem_id:
            return "", problem_id
        file_path = root_path / problem_folder / f"{problem_folder}_{problem_id}" / self.solution_file
        if not file_path.exists():
            return "", problem_id
        final_codes = deque([])
        with file_path.open("r", encoding="utf-8") as f:
            lines = f.read().split("\n")
            import_part = False
            for line in lines:
                logging.info(line)
                if line.startswith("package problem"):
                    continue
                if import_part:
                    if line.strip() == ")":
                        import_part = False
                    continue
                elif "import " in line:
                    import_part = True
                    continue
                if (
                        "func Solve(input string) any {" in line
                        or "func Solve(inputJsonValues string) any {" in line
                        or "func Solve(input string) interface{} {" in line
                        or "func Solve(inputJsonValues string) interface{} {" in line
                ):
                    break
                final_codes.append(line)
        while final_codes and final_codes[0].strip() == "":
            final_codes.popleft()
        return "\n".join(final_codes), problem_id

    @staticmethod
    def __process_inputs(
            code_default: str, input_str: str, struct_dict: dict, struct_func: bool, testcases=None
    ) -> Tuple[set, str, str, str, str, str]:
        res = []
        imports_libs = set()
        json_parse = []
        variables = []
        extra = ""
        end_extra = []
        if input_str.strip() == "":
            return set(), "", "", "", extra, ""
        splits = input_str.split(",")
        first = True
        list_type_vars = []
        for i, s in enumerate(splits):
            ss = s.split(" ")
            tmp_ss = []
            for tmp_s in ss:
                if tmp_s.strip() != "":
                    tmp_ss.append(tmp_s)
            variables.append(tmp_ss[0])
            if first:
                list_type_vars.append([])
                res.append("\tvar ")
            list_type_vars[-1].append(tmp_ss[0])
            if len(tmp_ss) != 2:
                res.append(tmp_ss[0])
                res.append(", ")
                first = False
            else:
                list_type_vars[-1].append(tmp_ss[1])
                res.append(tmp_ss[0])
                res.append(" ")
                tp = tmp_ss[1]
                res.append(tp)
                res.append("\n")
                first = True
        list_type_vars_new: List[List] = []
        total_vars = 0
        for vars_type in list_type_vars:
            logging.debug("Vars type: %s", vars_type)
            if list_type_vars_new and list_type_vars_new[-1][-1] == vars_type[-1]:
                list_type_vars_new[-1] = list_type_vars_new[-1][:-1]
                list_type_vars_new[-1].extend(vars_type)
            else:
                list_type_vars_new.append(vars_type)
            total_vars += len(vars_type) - 1
        logging.debug("Total vars: %d", total_vars)
        list_type_vars = list_type_vars_new
        logging.debug("List type vars: %s", list_type_vars)
        counts = 0
        if struct_func:
            variables = []
        count = 0
        for i, vars_type in enumerate(list_type_vars):
            vrs, tp = vars_type[:-1], vars_type[-1]
            if (tp.startswith("*") and tp[1:] in struct_dict) or tp in struct_dict:
                logging.debug("Golang unimplemented struct: ")
                for var in vrs:
                    logging.debug(var)
            elif struct_func:
                logging.debug("Struct function: %s", tp)
                imports_libs.add('\t"encoding/json"')
                imports_libs.add('\t"log"')
                for v in vrs:
                    match tp:
                        case "int":
                            variables.append(f"int(inputValues[{counts}].(float64))")
                        case "[]string":
                            extra += (f"var {v}Arr []string\n\t\t\tif v, ok := inputValues[{counts}].([]string); ok {{\n"
                                     f"\t\t\t\t{v}Arr = v\n\t\t\t}} else {{\n"
                                     f"\t\t\t\tfor _, vi := range inputValues[{counts}].([]any) {{\n"
                                     f"\t\t\t\t\t{v}Arr = append({v}Arr, vi.(string))\n"
                                     f"\t\t\t\t}}\n\t\t\t}}\n\t\t\t")
                            variables.append(f"{v}Arr")
                        case "[]int":
                            extra += (f"var {v}Arr []int\n\t\t\tif v, ok := inputValues[{counts}].([]int); ok {{\n"
                                        f"\t\t\t\t{v}Arr = v\n\t\t\t}} else {{\n"
                                        f"\t\t\t\tfor _, vi := range inputValues[{counts}].([]any) {{\n"
                                        f"\t\t\t\t\t{v}Arr = append({v}Arr, int(vi.(float64)))\n"
                                        f"\t\t\t\t}}\n\t\t\t}}\n\t\t\t")
                            variables.append(f"{v}Arr")
                        case "[][]int":
                            extra += (f"var {v}Arr [][]int\n\t\t\tif v, ok := inputValues[{counts}].([][]int); ok {{\n"
                                        f"\t\t\t\t{v}Arr = v\n\t\t\t}} else {{\n"
                                        f"\t\t\t\t{v}Arr = make([][]int, len(inputValues[{counts}].([]any)))\n"
                                        f"\t\t\t\tfor i := range {v}Arr {{\n"
                                        f"\t\t\t\t\t{v}Arr[i] = make([]int, len(inputValues[{counts}].([]any)[i].([]any)))\n"
                                        f"\t\t\t\t\tfor j := range {v}Arr[i] {{\n"
                                        f"\t\t\t\t\t\t\t\t{v}Arr[i][j] = int(inputValues[{counts}].([]any)[i].([]any)[j].(float64))\n"
                                        f"\t\t\t\t\t}}\n\t\t\t\t}}\n\t\t\t}}\n\t\t\t")
                            variables.append(f"{v}Arr")
                        case "*TreeNode" | "TreeNode":
                            imports_libs.add('\t. "leetCode/golang/models"')
                            variables.append(f"InterfaceArrayToTree(inputValues[{counts}].([]any))")
                        case _:
                            variables.append(f"inputValues[{counts}].({tp})")
                    counts += 1
            else:
                match tp:
                    case "*ListNode":
                        if testcases:
                            logging.debug(f"Testcases: {testcases}, variables: {vrs}")
                            if len(testcases[0]) == total_vars + 1 and all(
                                    isinstance(testcase[0], list)
                                    and isinstance(testcase[1], int)
                                    for testcase in testcases):
                                for j, var in enumerate(vrs):
                                    json_parse.append(f"\tvar {var}IntArray []int\n")
                                    json_parse.append(
                                        f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]), &"
                                        + var
                                        + "IntArray); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                                    )
                                    json_parse.append(f"\t var {var}Pos int\n")
                                    json_parse.append(
                                        f"\tif err := json.Unmarshal([]byte(inputValues[{count + len(vrs)}]),"
                                        f" &{var}Pos); err != nil {{\n\t\tlog.Fatal(err)\n\t}}\n"
                                    )
                                    json_parse.append(
                                        f"\t{var} = IntArrayToLinkedListCycle({var}IntArray, {var}Pos)\n"
                                    )
                                imports_libs.add('\t. "leetCode/golang/models"')
                                imports_libs.add('\t"encoding/json"')
                                imports_libs.add('\t"log"')
                                count += 2
                                continue
                            elif (total_vars == 2 and len(testcases[0]) == 5
                                  and all(isinstance(testcase[0], int) and
                                          isinstance(testcase[1], list) and
                                          isinstance(testcase[2], list) and
                                          isinstance(testcase[3], int) and
                                          isinstance(testcase[4], int) for testcase in
                                          testcases)):
                                json_parse.append("\tvar iv, idx1, idx2 int\n")
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[{count}]), &iv); err != nil {{\n"
                                    f"\t\tlog.Fatal(err)\n"
                                    f"\t}}\n"
                                )
                                json_parse.append(f"\tvar headAIntArray []int\n")
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[{count + 1}]), &headAIntArray);"
                                    f" err != nil {{\n\t\tlog.Fatal(err)\n\t}}\n"
                                )
                                json_parse.append(f"\tvar headBIntArray []int\n")
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[{count + 2}]), &headBIntArray);"
                                    f" err != nil {{\n\t\tlog.Fatal(err)\n\t}}\n"
                                )
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[{count + 3}]), &idx1);"
                                    f" err != nil {{\n\t\tlog.Fatal(err)\n\t}}\n"
                                )
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[{count + 4}]), &idx2);"
                                    f" err != nil {{\n\t\tlog.Fatal(err)\n\t}}\n"
                                )
                                json_parse.append("\theads := IntArrayToLinkedListIntersection(headAIntArray,"
                                                  " headBIntArray, iv, idx1, idx2)\n")
                                json_parse.append("\theadA, headB = heads[0], heads[1]\n")
                                imports_libs.add('\t. "leetCode/golang/models"')
                                imports_libs.add('\t"encoding/json"')
                                imports_libs.add('\t"log"')
                                count += 5
                                continue
                            elif total_vars != len(testcases[0]):
                                logging.debug(f"Testcases: {testcases}, variables: {vrs}")
                        for j, var in enumerate(vrs):
                            json_parse.append(f"\tvar {var}IntArray []int\n")
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]), &"
                                + var
                                + "IntArray); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                            )
                            json_parse.append(
                                f"\t{var} = IntArrayToLinkedList({var}IntArray)\n"
                            )
                        imports_libs.add('\t. "leetCode/golang/models"')
                        imports_libs.add('\t"encoding/json"')
                        imports_libs.add('\t"log"')
                    case "[]*ListNode":
                        for j, var in enumerate(vrs):
                            json_parse.append(f"\tvar {var}IntArrays [][]int\n")
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]), &"
                                + var
                                + "IntArrays); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                            )
                            json_parse.append(
                                f"\tfor i := 0; i < len({var}IntArrays); i++" + "{\n"
                            )
                            json_parse.append(
                                f"\t\t{var} = append({var}, IntArrayToLinkedList({var}IntArrays[i]))\n"
                            )
                            json_parse.append("\t}\n")
                        imports_libs.add('\t. "leetCode/golang/models"')
                        imports_libs.add('\t"encoding/json"')
                        imports_libs.add('\t"log"')
                    case "*TreeNode":
                        imports_libs.add('\t. "leetCode/golang/models"')
                        if testcases:
                            logging.debug(f"Testcases: {testcases}, variables: {vrs}")
                            if total_vars == len(testcases[0]) + 1:
                                imports_libs.add('\t"encoding/json"')
                                imports_libs.add('\t"log"')
                                json_parse.append("\tvar targetVal int\n")
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[1]), &targetVal); err != nil {{\n"
                                    f"\t\tlog.Fatal(err)\n"
                                    f"\t}}\n"
                                )
                                json_parse.append(f"\tnodes := ArrayToTreeAndTargets(inputValues[0], targetVal)\n")
                                json_parse.append(f"\t{vrs[0]}, {vrs[-1]} = nodes[0], nodes[1]\n")
                                json_parse.append(f"\t{vrs[1]} = ArrayToTree(inputValues[0])\n")
                                count += len(vrs)
                                continue
                            elif total_vars > 1 and len(list_type_vars) == 1 and any(t is not None and not isinstance(t, list)
                                                        for testcase in testcases for t in testcase):
                                imports_libs.add('\t"encoding/json"')
                                imports_libs.add('\t"log"')
                                j = last_idx = 0

                                while j <= len(vrs):
                                    if j < len(vrs) and any(testcase[j] is not None
                                                            and not isinstance(testcase[j], list)
                                                            for testcase in testcases):
                                        json_parse.append(f"\tvar targetVal{count + j} int\n")
                                        json_parse.append(
                                            f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]),"
                                            f" &targetVal{count + j} ); err != nil {{\n"
                                            f"\t\tlog.Fatal(err)\n"
                                            f"\t}}\n"
                                        )
                                    elif j:
                                        json_parse.append(f"\tnodes := ArrayToTreeAndTargets(inputValues[{last_idx}], "
                                                          + ", ".join([f"targetVal{count + idx}"
                                                                       for idx in range(last_idx + 1, j)])
                                                          + ")\n")
                                        json_parse.append(f"\t{vrs[last_idx]},"
                                                          f" {', '.join(vrs[idx] for idx in range(last_idx + 1, j))}"
                                                          f" = nodes[0], {', '.join(
                                                              f'nodes[{idx}]' for idx in range(1, j - last_idx))}\n")
                                        last_idx = j
                                    j += 1
                                count += len(vrs)
                                continue
                        for j, var in enumerate(vrs):
                            json_parse.append(f"\t{var} = ArrayToTree(inputValues[{count + j}])\n")
                    case "[]*TreeNode":
                        for j, var in enumerate(vrs):
                            json_parse.append(
                                f"\t{var} = ArrayToTreeArray(inputValues[{count + j}])\n"
                            )
                        imports_libs.add('\t. "leetCode/golang/models"')
                    case "*Node":
                        if (
                                "Left *Node" in code_default
                                and "Right *Node" in code_default
                                and "Next *Node" in code_default
                        ):
                            for j, var in enumerate(vrs):
                                json_parse.append(
                                    f"\t{var} = ArrayToTreeNext(inputValues[{count + j}])\n"
                                )
                            imports_libs.add('\t. "leetCode/golang/tree_next"')
                        elif "Neighbors []*Node" in code_default:
                            for j, var in enumerate(vrs):
                                json_parse.append("\tvar arr" + f"{count + j}" + " [][]int\n")
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]), &"
                                    + f"arr{count + j}"
                                    + "); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                                )
                                json_parse.append(
                                    f"\t{var} = ArrayRelationToNodeNeighbour(arr{count + j})\n"
                                )
                            imports_libs.add('\t. "leetCode/golang/node_neighbours"')
                            imports_libs.add('\t"encoding/json"')
                            imports_libs.add('\t"log"')
                        elif (
                                "/**\n"
                                " * Definition for a Node.\n"
                                " * type Node struct {\n"
                                " *     Val int\n"
                                " *     Next *Node\n"
                                " *     Random *Node\n"
                                " * }\n"
                                " */" in code_default
                        ):
                            for j, var in enumerate(vrs):
                                json_parse.append(
                                    "\tvar arr" + f"{count + j}" + " [][]any\n"
                                )
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]), &"
                                    + f"arr{count + j}"
                                    + "); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                                )
                                json_parse.append(
                                    f"\t{var} = IntRandomArrayToNodeArray(arr{count + j})\n"
                                )
                            imports_libs.add('\t. "leetCode/golang/node_random"')
                            imports_libs.add('\t"encoding/json"')
                            imports_libs.add('\t"log"')
                    case "[]byte":
                        for j, var in enumerate(vrs):
                            json_parse.append(f"\tvar {var}Str []string\n")
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]), &"
                                + var
                                + "Str); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                            )
                            json_parse.append(
                                f"\t{var} = make([]byte, len({var}Str))\n"
                            )
                            json_parse.append(
                                "\tfor i := 0; i < len(" + var + "); i++ {\n"
                            )
                            json_parse.append(f"\t\t{var}[i] = {var}Str[i][0]\n")
                            json_parse.append("\t}\n")
                        end_extra.append("func byteArrToStrArr(arr []byte) []string {")
                        end_extra.append("\tans := make([]string, len(arr))")
                        end_extra.append("\tfor i, b := range arr {")
                        end_extra.append("\t\tans[i] = string(b)")
                        end_extra.append("\t}")
                        end_extra.append("\treturn ans")
                        end_extra.append("}")
                        imports_libs.add('\t"encoding/json"')
                        imports_libs.add('\t"log"')
                    case "[][]byte":
                        for j, var in enumerate(vrs):
                            json_parse.append(f"\tvar {var}Str [][]string\n")
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]), &"
                                + var
                                + "Str); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                            )
                            json_parse.append(
                                f"\t{var} = make([][]byte, len({var}Str))\n"
                            )
                            json_parse.append(
                                "\tfor i := 0; i < len(" + var + "); i++ {\n"
                            )
                            json_parse.append(
                                f"\t\t{var}[i] = make([]byte, len({var}Str[i]))\n"
                            )
                            json_parse.append(
                                "\t\tfor j := 0; j < len(" + var + "[i]); j++ {\n"
                            )
                            json_parse.append(
                                f"\t\t\t{var}[i][j] = {var}Str[i][j][0]\n"
                            )
                            json_parse.append("\t\t}\n")
                            json_parse.append("\t}\n")
                        end_extra.append("func byteArrToStrArr(arr [][]byte) []string {")
                        end_extra.append("\tans := make([]string, len(arr))")
                        end_extra.append("\tfor i, b := range arr {")
                        end_extra.append("\t\tans[i] = string(b)")
                        end_extra.append("\t}")
                        end_extra.append("\treturn ans")
                        end_extra.append("}")
                        imports_libs.add('\t"encoding/json"')
                        imports_libs.add('\t"log"')
                    case "byte":
                        for j, var in enumerate(vrs):
                            json_parse.append(f"\tvar {var}Str string\n")
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]), &"
                                + var
                                + "Str); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                            )
                            json_parse.append(f"\tif len({var}Str) > 1 " + "{\n")
                            json_parse.append(f"\t\t{var} = {var}Str[1]\n")
                            json_parse.append("\t} else {\n")
                            json_parse.append(f"\t\t{var} = {var}Str[0]\n")
                            json_parse.append("\t}\n")
                        imports_libs.add('\t"encoding/json"')
                        imports_libs.add('\t"log"')
                    case _:
                        logging.debug("Unhandled type %s", tp)
                        pure_type = "".join(c for c in tp if c.isalnum())
                        logging.debug("Pure type: %s", pure_type)
                        if (index := code_default.find(f"Definition for {pure_type}")) != -1:
                            logging.debug("Add definition for %s, idx: %d", pure_type, index)
                            # extract comment code definition at back
                            end_index = code_default.find("*/", index)
                            logging.debug("Code content:\n%s", code_default[index:end_index])
                            for i, line in enumerate(code_default[index:end_index].split("\n")):
                                line = line.strip()
                                if i == 0:
                                    end_extra.append(f"// {line}")
                                    continue
                                line_start = 0
                                if line.startswith("*"):
                                    while line_start < len(line) and line[line_start] == "*":
                                        line_start += 1
                                    if line[line_start] == " ":
                                        line_start += 1
                                end_extra.append(line[line_start:])
                            logging.debug("End extra: %s", end_extra)
                            end_extra.append(f"func constructor(input any) *{pure_type} {{")
                            end_extra.append("\treturn nil")
                            end_extra.append("}")
                            logging.debug("Vars: %s", vrs)
                            if tp == pure_type or tp == f"*{pure_type}":
                                for j, var in enumerate(vrs):
                                    json_parse.append(f"\t{var} = constructor(inputValues[{count + j}])\n")
                            elif "[]" in tp:
                                for j, var in enumerate(vrs):
                                    json_parse.append(f"\tvar {var}_input_array []any\n")
                                    json_parse.append(
                                        f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]), &"
                                        + var
                                        + "_input_array); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                                    )
                                    json_parse.append(f"\tfor _, ipt := range {var}_input_array {{\n")
                                    json_parse.append(f"\t\t{var} = append({var}, constructor(ipt))\n")
                                    json_parse.append("\t}\n")
                        else:
                            for j, var in enumerate(vrs):
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[{count + j}]), &"
                                    + var
                                    + "); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                                )
                        imports_libs.add('\t"encoding/json"')
                        imports_libs.add('\t"log"')
            count += len(vrs)
        imports_libs.add('\t"strings"')
        return imports_libs, "".join(res), "".join(json_parse), ", ".join(variables), extra, "\n".join(end_extra)
