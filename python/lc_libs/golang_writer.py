import os.path
from collections import deque
from typing import Tuple

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
                str(os.path.join(self.main_folder, self.test_file)),
                str(os.path.join(self.main_folder, self.basic_package_file)),
            ]
        ]

    def change_test(self, root_path, problem_folder: str, question_id: str):
        with open(os.path.join(root_path, self.main_folder, self.test_file), "w") as f:
            f.write(
                TESTCASE_TEMPLATE_GOLANG.format(
                    f'problem "leetCode/{problem_folder}/{problem_folder}_{question_id}"',
                    "TestSolution",
                    f'TestEach(t, "{question_id}", "{problem_folder}", problem.Solve)',
                )
            )

    def change_tests(self, root_path, problem_ids_folders: list):
        with open(os.path.join(root_path, self.main_folder, self.tests_file), "w") as f:
            f.write(
                TESTCASE_TEMPLATE_GOLANG.format(
                    "\n\t".join(
                        f'"leetCode/{pf}/{pf}_{pid}"' for pid, pf in problem_ids_folders
                    ),
                    "TestSolutions",
                    "\n\t".join(
                        f'TestEach(t, "{pid}", "{pf}", problem{pid}.Solve)'
                        for pid, pf in problem_ids_folders
                    ),
                )
            )

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
        for i, line in enumerate(code_default.split("\n")):
            line = line.strip()
            if line.startswith("func "):
                rts.append(line.split("{")[0].split(")")[-1].strip())
                its.append(
                    GolangWriter.__process_inputs(
                        code_default, line.split("(")[1].split(")")[0], structs_map
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
                        tp0, tp1, tp2, tp3 = GolangWriter.__process_inputs(
                            code_default,
                            tmp.split("(")[1].split(")")[0],
                            structs_map,
                            True,
                        )
                        rt = tmp.split("{")[0].split(")")[-1].strip()
                        structs_map[struct_name]["construct"] = (
                            tmp.split("(")[0].split("func ")[-1].strip(),
                            (tp0, tp1, tp2, tp3.replace("inputValues", "opValues[0]")),
                            rt,
                        )
                    elif tmp.startswith("func (") and struct_name in tmp.split(")")[0]:
                        if "funcs" not in structs_map[struct_name]:
                            structs_map[struct_name]["funcs"] = []
                        tp0, tp1, tp2, tp3 = GolangWriter.__process_inputs(
                            code_default,
                            tmp.split("(")[2].split(")")[0],
                            structs_map,
                            True,
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
                                ),
                                rt,
                            )
                        )

                import_set = set()
                func_loop = ""
                constructor = None
                for d in structs_map.values():
                    if "funcs" in d:
                        for name, its, rt in d["funcs"]:
                            import_set.update(its[0])
                            func_loop += (
                                '\t\tcase "{}", "{}":\n' "\t\t\t{}obj.{}({})\n"
                            ).format(
                                name[0].lower() + name[1:],
                                name,
                                "res = nil\n\t\t\t" if rt == "" else "res = ",
                                name,
                                its[3],
                            )
                    if "construct" in d:
                        constructor = d["construct"]
                build_body = (
                        "\tvar operators []string\n"
                        + "\tvar opValues [][]interface{}\n"
                        + "\tvar ans []interface{}\n"
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
                        "\tobj :=" + constructor[0] + f"({constructor[1][3]})\n"
                        if constructor is not None
                        else ""
                    ),
                    "",
                )
                        + "\tans = append(ans, nil)\n"
                        + "\tfor i := 1; i < len(operators); i++ {\n"
                        + "\t\tvar res interface{}\n"
                        + "{}".format(
                    "\t\tswitch operators[i] {\n" + func_loop + "\t\tdefault:\n"
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
                    code_default if not code else code,
                    build_body,
                    "",
                    "ans",
                    "",
                ).replace("return ans()", "return ans")
        import_set = set()
        for it in its:
            import_set.update(it[0])

        if (
                len(rts) != 1
                or rts[0] == "*TreeNode"
                or rts[0] == "*ListNode"
                or rts[0] == "*Node"
        ):
            return_func_var = "{}({})".format(
                func_names[0], ", ".join(list(zip(*its))[3])
            )
            match rts[0]:
                case "*TreeNode":
                    return_func_name = "TreeToArray"
                case "*ListNode":
                    return_func_name = return_func_var + ".LinkedListToIntArray"
                    return_func_var = ""
                case "*Node":
                    return_func_name = "ToBeImplemented"
                    if (
                            "Left *Node" in code_default
                            and "Right *Node" in code_default
                            and "Next *Node" in code_default
                    ):
                        return_func_name = "TreeNextToArray"
                    elif "Neighbors []*Node" in code_default:
                        return_func_name = "NodeNeighbourToArrayRelation"
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
                        return_func_name = "NodeArrayToIntRandomArray"
                case _:
                    return_func_name = ""

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
                code_default if not code else code,
                "\n".join(list(zip(*its))[1]),
                "\n".join(list(zip(*its))[2]),
                return_func_name,
                return_func_var,
            )
        if rts[0] == "":
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
                its[0][3],
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
            code_default if not code else code,
            "\n".join(list(zip(*its))[1]),
            "\n".join(list(zip(*its))[2]),
            func_names[0],
            ", ".join(list(zip(*its))[3]),
        )

    def get_solution_code(
            self, root_path, problem_folder: str, problem_id: str
    ) -> Tuple[str, str]:
        if not problem_id:
            with open(
                    os.path.join(root_path, "golang", "solution_test.go"),
                    "r",
                    encoding="utf-8",
            ) as f:
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
        file_path = os.path.join(
            root_path, problem_folder, f"{problem_folder}_{problem_id}", "solution.go"
        )
        if not os.path.exists(file_path):
            return "", problem_id
        final_codes = deque([])
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.read().split("\n")
            import_part = False
            for line in lines:
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
                        "func Solve(input string) interface{} {" in line
                        or "func Solve(inputJsonValues string) interface{} {" in line
                ):
                    break
                final_codes.append(line)
        while final_codes and final_codes[0].strip() == "":
            final_codes.popleft()
        return "\n".join(final_codes), problem_id

    @staticmethod
    def __process_inputs(
            code_default: str, input_str: str, struct_dict: dict, struct_func: bool = False
    ) -> Tuple[set, str, str, str]:
        res = []
        imports_libs = set()
        json_parse = []
        variables = []
        if input_str.strip() == "":
            return set(), "", "", ""
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
        counts = 0
        if struct_func:
            variables = []
        for i, vars_type in enumerate(list_type_vars):
            vrs, tp = vars_type[:-1], vars_type[-1]
            if (tp.startswith("*") and tp[1:] in struct_dict) or tp in struct_dict:
                for var in vrs:
                    print(var)
            elif struct_func:
                imports_libs.add('\t"encoding/json"')
                imports_libs.add('\t"log"')
                for _ in vrs:
                    (
                        variables.append(f"inputValues[{counts}].({tp})")
                        if tp != "int"
                        else variables.append(f"int(inputValues[{counts}].(float64))")
                    )
                    counts += 1
            else:
                match tp:
                    case "*ListNode":
                        for var in vrs:
                            json_parse.append(f"\tvar {var}IntArray []int\n")
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{i}]), &"
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
                        for var in vrs:
                            json_parse.append(f"\tvar {var}IntArrays [][]int\n")
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{i}]), &"
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
                        for var in vrs:
                            json_parse.append(
                                f"\t{var} = ArrayToTree(inputValues[{i}])\n"
                            )
                        imports_libs.add('\t. "leetCode/golang/models"')
                    case "[]*TreeNode":
                        for var in vrs:
                            json_parse.append(
                                f"\t{var} = ArrayToTreeArray(inputValues[{i}])\n"
                            )
                        imports_libs.add('\t. "leetCode/golang/models"')
                    case "*Node":
                        if (
                                "Left *Node" in code_default
                                and "Right *Node" in code_default
                                and "Next *Node" in code_default
                        ):
                            for var in vrs:
                                json_parse.append(
                                    f"\t{var} = ArrayToTree(inputValues[{i}])\n"
                                )
                            imports_libs.add('\t. "leetCode/golang/tree_next"')
                        elif "Neighbors []*Node" in code_default:
                            for var in vrs:
                                json_parse.append("\tvar arr" + f"{i}" + " [][]int\n")
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[{i}]), &"
                                    + f"arr{i}"
                                    + "); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                                )
                                json_parse.append(
                                    f"\t{var} = ArrayRelationToNodeNeighbour(arr{i})\n"
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
                            for var in vrs:
                                json_parse.append(
                                    "\tvar arr" + f"{i}" + " [][]interface{}\n"
                                )
                                json_parse.append(
                                    f"\tif err := json.Unmarshal([]byte(inputValues[{i}]), &"
                                    + f"arr{i}"
                                    + "); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                                )
                                json_parse.append(
                                    f"\t{var} = IntRandomArrayToNodeArray(arr{i})\n"
                                )
                            imports_libs.add('\t. "leetCode/golang/node_random"')
                            imports_libs.add('\t"encoding/json"')
                            imports_libs.add('\t"log"')
                    case "[]byte":
                        for var in vrs:
                            json_parse.append(f"\tvar {var}Str []string\n")
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{i}]), &"
                                + var
                                + "Str); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                            )
                            json_parse.append(
                                f"\t{var} := make([]byte, len({var}Str))\n"
                            )
                            json_parse.append(
                                "\tfor i := 0; i < len(" + var + "); i++ {\n"
                            )
                            json_parse.append(f"\t\t{var}[i] = {var}Str[i][0]\n")
                            json_parse.append("\t}\n")
                    case "[][]byte":
                        for var in vrs:
                            json_parse.append(f"\tvar {var}Str [][]string\n")
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{i}]), &"
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
                        imports_libs.add('\t"encoding/json"')
                        imports_libs.add('\t"log"')
                    case "byte":
                        for var in vrs:
                            json_parse.append(f"\tvar {var}Str string\n")
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{i}]), &"
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
                        for var in vrs:
                            json_parse.append(
                                f"\tif err := json.Unmarshal([]byte(inputValues[{i}]), &"
                                + var
                                + "); err != nil {\n\t\tlog.Fatal(err)\n\t}\n"
                            )
                        imports_libs.add('\t"encoding/json"')
                        imports_libs.add('\t"log"')
        imports_libs.add('\t"strings"')
        return imports_libs, "".join(res), "".join(json_parse), ", ".join(variables)
