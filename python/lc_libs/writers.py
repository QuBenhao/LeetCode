import inspect
import os
import traceback
from collections import defaultdict
from importlib.util import spec_from_file_location, module_from_spec
from constants import TESTCASE_TEMPLATE_PYTHON, TESTCASE_TEMPLATE_PYTHON_TESTCASES, SOLUTION_TEMPLATE_PYTHON


def write_problem_md(question_id: str, question_name: str, desc: str) -> str:
    check = False
    formated = []
    for line in desc.split("\n"):
        if "<ul>" in line:
            check = True
        elif "</ul>" in line:
            check = False
        elif check and len(line) == 0:
            continue
        formated.append(line)
    return "# {}. {}\n\n{}".format(question_id, question_name, "\n".join(formated))


def write_testcase(testcases, outputs) -> str:
    res = ""
    for inputs, output in zip(testcases, outputs):
        res += (TESTCASE_TEMPLATE_PYTHON_TESTCASES
                .format(f"\"{inputs}\"" if isinstance(inputs, str) else inputs,
                        f"\"{output}\"" if isinstance(output, str) else output))
    return TESTCASE_TEMPLATE_PYTHON.format(res)


def __process_code(code: str):
    top = []
    res = []
    process_class = False
    top.append("from typing import *\n")
    splits = code.split("\n")
    idx = 0
    while idx < len(splits):
        line = splits[idx]
        if "# class " in line:
            process_class = True
            top.append(line[2:])
            idx += 1
            continue
        elif process_class:
            if line.startswith("#"):
                top.append(line[2:])
                idx += 1
                continue
            else:
                process_class = False
        if ('"""' in line and idx < len(splits) - 1 and
                (splits[idx + 1].strip().startswith("class ") or splits[idx + 1].strip().startswith("# "))):
            idx += 1
            while idx < len(splits) and '"""' not in splits[idx]:
                if "from typing import " not in res:
                    res.append(splits[idx])
                idx += 1
            idx += 1
            continue
        if "from typing import " in line:
            idx += 1
            continue
        res.append(line)
        sl = line.strip()
        if sl.startswith("def ") and sl.endswith(":"):
            if idx < len(splits) - 1 and '"""' in splits[idx + 1]:
                idx += 1
                while idx < len(splits) - 1 and '"""' not in splits[idx + 1].strip():
                    res.append(splits[idx])
                    idx += 1
                res.append(splits[idx])
                idx += 1
                res.append(splits[idx])
                sp = splits[idx].count(" ", None, splits[idx].index('"""'))
                sp = (sp + 3) // 4 * 4
            else:
                sp = line.count(" ", line.index("def "))
                sp = (sp + 3) // 4 * 4 + 4
            res.append(sp * " " + "pass")
        idx += 1
    with open("tmp.py", "w", encoding="utf-8") as f:
        f.writelines("\n".join(top) + "\n\n")
        f.writelines("\n".join(res))
    solution_spec = spec_from_file_location("module.name", f"tmp.py")
    solution = module_from_spec(solution_spec)
    solution_spec.loader.exec_module(solution)
    classes = inspect.getmembers(solution, inspect.isclass)
    your_classes = [c for c in classes if c[1].__module__ == solution.__name__]

    cs_map = defaultdict(list)
    for cs in your_classes:
        class_name = cs[0]
        # Get the method of your class
        methods = inspect.getmembers(cs[1], inspect.isroutine)

        # TODO: Fix issues like 382, the external class is called Solution
        # Filter out in-built dunder methods
        non_dunder_methods = [
            m for m in methods
            if m[0] == "__init__" or not (m[0].startswith('__') and m[0].endswith('__'))]

        for method in non_dunder_methods:
            md = getattr(cs[1], method[0])
            sig = inspect.signature(md)
            if cs[0] == "Solution" and method[0] == "__init__":
                d = dict(sig.parameters)
                counts = len(d)
                if "self" in d:
                    counts -= 1
                if "args" in d:
                    counts -= 1
                if "kwargs" in d:
                    counts -= 1
                if counts == 0:
                    continue
                if class_name in cs_map:
                    cs_map["S"] = list(cs_map[class_name])
                    cs_map.pop(class_name)
                class_name = "S"
                for i, line in enumerate(res):
                    if "class Solution" in line:
                        res[i] = line.replace("Solution", "S")
            cs_map[class_name].append((method[0], dict(sig.parameters), sig.return_annotation))

    os.remove("tmp.py")
    return cs_map, top, res


def __finalize_solution_code(cs_map, top, res, modify_in_place):
    process_input = "pass"
    if len(cs_map) == 1:
        if "Solution" in cs_map:
            methods = cs_map["Solution"]
            if len(methods) == 1:
                parameters, return_anno = methods[0][1], methods[0][2]
                count = len(parameters)
                if "self" in parameters:
                    count -= 1
                if "args" in parameters:
                    count -= 1
                if "kwargs" in parameters:
                    count -= 1
                if count > 1:
                    init_params = "*test_input"
                elif count == 1:
                    init_params = "test_input"
                else:
                    init_params = ""
                if not modify_in_place:
                    process_input = "return self.{}({})".format(methods[0][0], init_params)
                else:
                    process_input = "self.{}({})\n        return {}".format(methods[0][0], init_params, init_params)
        else:
            class_name, methods = "", []
            for k, v in cs_map.items():
                class_name, methods = k, v
            top[0] = top[0] + "from python.object_libs import call_method\n"
            init_params = ""
            for method in methods:
                if method[0] == "__init__":
                    parameters, return_anno = methods[0][1], methods[0][2]
                    count = len(parameters)
                    if "self" in parameters:
                        count -= 1
                    if "args" in parameters:
                        count -= 1
                    if "kwargs" in parameters:
                        count -= 1
                    if count > 0:
                        init_params = "*inputs[0]"
                    break

            process_input = (("ops, inputs = test_input\n        obj = {}({})\n        return [None] + "
                              "[call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]")
                             .format(class_name, init_params))
    else:
        if "Solution" in cs_map:
            methods = cs_map["Solution"]
            if len(methods) == 1:
                parameters, return_anno = methods[0][1], methods[0][2]
                par_map = dict()
                add_lib = ""
                exists = False
                process_input = ""
                remain = ""
                inputs = ""
                is_first = True
                idx = 0
                for v in parameters.values():
                    if v.name == "self":
                        continue
                    if v.name == "args":
                        continue
                    if v.name == "kwargs":
                        continue
                    par_map[v.name] = v.annotation
                    if is_first:
                        is_first = False
                    else:
                        process_input += ", "
                        inputs += ", "
                    if "TreeNode" in str(v.annotation):
                        exists = True
                        add_lib = "from python.object_libs import list_to_tree"
                        if "List[" in str(v.annotation):
                            process_input += "nums_arr"
                            remain += "        roots = [list_to_tree(nums) for nums in nums_arr]\n"
                            inputs += "roots"
                        else:
                            process_input += f"nums{idx}"
                            remain += f"        root{idx} = list_to_tree(nums{idx})\n"
                            inputs += f"root{idx}"
                            idx += 1
                    elif "ListNode" in str(v.annotation):
                        exists = True
                        add_lib = "from python.object_libs import list_to_linked_list"
                        if "List[" in str(v.annotation):
                            process_input += "nums_arr"
                            remain += f"        heads = [list_to_linked_list(nums) for nums in nums_arr]\n"
                            inputs += "heads"
                        else:
                            process_input += f"nums{idx}"
                            remain += f"        head{idx} = list_to_linked_list(nums{idx})\n"
                            inputs += f"head{idx}"
                            idx += 1
                    else:
                        process_input += v.name
                        inputs += v.name
                        idx += 1

                if len(parameters) > 0:
                    process_input += " = test_input\n"

                if "TreeNode" in str(return_anno):
                    add_lib += ", tree_to_list" if exists else "from python.object_libs import tree_to_list"
                    if "List[" in str(return_anno):
                        remain += ("        res = self.{}({})\n        return [tree_to_list(root) for root in res]"
                                   .format(methods[0][0], inputs))
                    else:
                        remain += ("        res = self.{}({})\n        return tree_to_list(res)"
                                   .format(methods[0][0], inputs))
                elif "ListNode" in str(return_anno):
                    add_lib += ", linked_list_to_list" if exists else "from python.object_libs import linked_list_to_list"
                    if "List[" in str(return_anno):
                        remain += ("res = self.{}({})\n        return [linked_list_to_list(head) for head in "
                                   "res]").format(methods[0][0], inputs)
                    else:
                        remain += ("        res = self.{}({})\n        return linked_list_to_list(res)"
                                   .format(methods[0][0], inputs))
                else:
                    if not modify_in_place:
                        remain += "        return self.{}({})".format(methods[0][0], inputs)
                    else:
                        remain += "        self.{}({})\n        return {}".format(methods[0][0], inputs, inputs)
                top[0] = top[0] + add_lib + "\n"

                process_input += remain
        else:
            top[0] = top[0] + "from python.object_libs import call_method"
            if "TreeNode" in cs_map:
                top[0] += ", list_to_tree"
                cs_map.pop("TreeNode")
            elif "ListNode" in cs_map:
                top[0] += ", list_to_linked_list"
                cs_map.pop("ListNode")
            else:
                # Too complex to fix here
                pass
            top[0] += "\n"
            if len(cs_map) == 1:
                class_name, methods = "", []
                for k, v in cs_map.items():
                    class_name, methods = k, v
                for method in methods:
                    if method[0] == "__init__":
                        parameters = methods[0][1]
                        par_map = dict()
                        process_input = "ops, inputs = test_input\n"
                        remain = ""
                        inputs = ""
                        is_first = True
                        idx = 0
                        for v in parameters.values():
                            if v.name == "self":
                                continue
                            if v.name == "args":
                                continue
                            if v.name == "kwargs":
                                continue
                            par_map[v.name] = v.annotation
                            if is_first:
                                is_first = False
                                process_input += "        "
                            else:
                                process_input += ", "
                                inputs += ", "
                            if "TreeNode" in str(v.annotation):
                                if "List[" in str(v.annotation):
                                    process_input += "nums_arr"
                                    remain += "        roots = [list_to_tree(nums) for nums in nums_arr]\n"
                                    inputs += "roots"
                                else:
                                    process_input += f"nums{idx}"
                                    remain += f"        root{idx} = list_to_tree(nums{idx})\n"
                                    inputs += f"root{idx}"
                                    idx += 1
                            elif "ListNode" in str(v.annotation):
                                if "List[" in str(v.annotation):
                                    process_input += "nums_arr"
                                    remain += f"        heads = [list_to_linked_list(nums) for nums in nums_arr]\n"
                                    inputs += "heads"
                                else:
                                    process_input += f"nums{idx}"
                                    remain += f"        head{idx} = list_to_linked_list(nums{idx})\n"
                                    inputs += f"head{idx}"
                                    idx += 1
                            else:
                                process_input += v.name
                                inputs += v.name
                                idx += 1

                        if len(par_map) > 0:
                            process_input += " = ops[0]\n"

                        process_input += remain + f"        obj = {class_name}({inputs})\n"
                        break

                process_input += ("        return [None] + [call_method(obj, op, *ipt)"
                                  " for op, ipt in zip(ops[1:], inputs[1:])]")

    top[0] = "import solution\n" + top[0]
    found = False
    for i, line in enumerate(res):
        if "class Solution" in line:
            res[i] = ("class Solution(solution.Solution):\n"
                      "    def solve(self, test_input=None):\n"
                      "        {}\n").format(process_input)
            found = True
            break
    if not found:
        res = ["class Solution(solution.Solution):\n"
               "    def solve(self, test_input=None):\n"
               "        {}\n".format(process_input)] + res
    return top, res


def __write_solution_python_backup(code: str):
    strip_code = []
    define_class = []
    if '"""' in code:
        sp = code.split('"""')
        code_source = ""
        for i in range(1, len(sp), 2):
            define_class.append(sp[i])
        for i in range(0, len(sp), 2):
            code_source += sp[i]
        for line in code_source.split("\n"):
            if line.startswith("from typing import"):
                continue
            if line.startswith("class Solution"):
                continue
            if len(line) > 0:
                strip_code.append(line)
    elif "class Solution" in code or "# class" in code:
        start = False
        strip_start = False
        for line in code.split("\n"):
            if line.startswith("from typing import"):
                continue
            if line.startswith("# class"):
                start = True
            if line.startswith("#"):
                if start:
                    define_class.append(line[2:])
                else:
                    if not strip_start:
                        define_class.append(line)
                    else:
                        strip_code.append(line)
                strip_start = False
            else:
                if strip_start:
                    strip_code.append(line)
                if line.startswith("class Solution"):
                    strip_start = True
                start = False
    return SOLUTION_TEMPLATE_PYTHON.format(
        "\n\n" + "\n".join(define_class) + "\n" if define_class else "",
        "pass",
        "\n".join(strip_code) if strip_code else code
    )


def write_solution_python(code: str, default: bool = True) -> str:
    if not default:
        if "class Solution" in code:
            return "\n".join(code.split("class Solution")[-1].split("\n")[1:])
        return code
    try:
        cs_map, top, res = __process_code(code)
        top, res = __finalize_solution_code(cs_map, top, res, "Do not return anything" in code)

        return "\n".join(top) + "\n\n" + "\n".join(res)
    except Exception as e:
        print("Exception raised:", e)
        traceback.print_exc()
        if os.path.exists("tmp.py"):
            os.remove("tmp.py")
    return __write_solution_python_backup(code)


def write_solution_golang(code_default: str, problem_id: str, default: bool = True, code: str = "") -> str:
    base_str = ("package problem{}\n\n"
                "import (\n"
                "{}\n"
                ")\n\n"
                "{}\n\n"
                "func Solve(input string) {}\n"
                "\tvalues := strings.Split(input, \"\\n\")\n"
                "{}\n{}\n"
                "\treturn {}({})\n{}\n"
                )

    def process_inputs(input_str: str, struct_dict: dict, struct_func: bool = False) -> (set, str, str, str):
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
        cnts = 0
        if struct_func:
            variables = []
        for i, vars_type in enumerate(list_type_vars):
            vrs, tp = vars_type[:-1], vars_type[-1]
            if (tp.startswith("*") and tp[1:] in struct_dict) or tp in struct_dict:
                for var in vrs:
                    print(var)
            elif struct_func:
                imports_libs.add("\t\"encoding/json\"")
                imports_libs.add("\t\"log\"")
                for _ in vrs:
                    variables.append(f"values[{cnts}].({tp})") if tp != "int" else variables.append(
                        f"int(values[{cnts}].(float64))")
                    cnts += 1
            else:
                match tp:
                    case "*ListNode":
                        for var in vrs:
                            json_parse.append(f"\tvar {var}IntArray []int\n")
                            json_parse.append(f"\tif err := json.Unmarshal([]byte(values[{i}]), &" + var +
                                              "IntArray); err != nil {\n\t\tlog.Fatal(err)\n\t}\n")
                            json_parse.append(f"\t{var} = IntArrayToLinkedList({var}IntArray)\n")
                        imports_libs.add("\t. \"leetCode/golang/models\"")
                        imports_libs.add("\t\"encoding/json\"")
                        imports_libs.add("\t\"log\"")
                    case "*TreeNode":
                        for var in vrs:
                            json_parse.append(f"\t{var} = ArrayToTree(values[{i}])\n")
                        imports_libs.add("\t. \"leetCode/golang/models\"")
                    case "*Node":
                        if ("Left *Node" in code_default
                                and "Right *Node" in code_default
                                and "Next *Node" in code_default):
                            for var in vrs:
                                json_parse.append(f"\t{var} = ArrayToTree(values[{i}])\n")
                            imports_libs.add("\t. \"leetCode/golang/tree_next\"")
                        elif "Neighbors []*Node" in code_default:
                            for var in vrs:
                                json_parse.append("\tvar arr" + f"{i}" + " [][]int\n")
                                json_parse.append(f"\tif err := json.Unmarshal([]byte(values[{i}]), &" + f"arr{i}" +
                                                  "); err != nil {\n\t\tlog.Fatal(err)\n\t}\n")
                                json_parse.append(f"\t{var} = ArrayRelationToNodeNeighbour(arr{i})\n")
                            imports_libs.add("\t. \"leetCode/golang/node_neighbours\"")
                            imports_libs.add("\t\"encoding/json\"")
                            imports_libs.add("\t\"log\"")
                        elif "/**\n" \
                             " * Definition for a Node.\n" \
                             " * type Node struct {\n" \
                             " *     Val int\n" \
                             " *     Next *Node\n" \
                             " *     Random *Node\n" \
                             " * }\n" \
                             " */" in code_default:
                            for var in vrs:
                                json_parse.append("\tvar arr" + f"{i}" + " [][]interface{}\n")
                                json_parse.append(f"\tif err := json.Unmarshal([]byte(values[{i}]), &" + f"arr{i}" +
                                                  "); err != nil {\n\t\tlog.Fatal(err)\n\t}\n")
                                json_parse.append(f"\t{var} = IntRandomArrayToNodeArray(arr{i})\n")
                            imports_libs.add("\t. \"leetCode/golang/node_random\"")
                            imports_libs.add("\t\"encoding/json\"")
                            imports_libs.add("\t\"log\"")
                    case _:
                        for var in vrs:
                            json_parse.append(f"\tif err := json.Unmarshal([]byte(values[{i}]), &" + var +
                                              "); err != nil {\n\t\tlog.Fatal(err)\n\t}\n")
                        imports_libs.add("\t\"encoding/json\"")
                        imports_libs.add("\t\"log\"")
        imports_libs.add("\t\"strings\"")
        return imports_libs, "".join(res), "".join(json_parse), ", ".join(variables)

    its = []
    rts = []
    func_names = []
    structs_map = dict()
    for i, line in enumerate(code_default.split("\n")):
        line = line.strip()
        if line.startswith("func "):
            rts.append(line.split("{")[0].split(")")[-1].strip())
            its.append(process_inputs(line.split("(")[1].split(")")[0], structs_map))
            func_names.append(line.split("(")[0].split("func ")[-1].strip())
        elif line.startswith("type ") and line.endswith(" struct {"):
            struct_name = line[len("type "):-len(" struct {")]
            structs_map[struct_name] = dict()
            for tmp in code_default.split("\n"):
                tmp = tmp.strip()
                if tmp.startswith("func ") and (
                        tmp.endswith(f") {struct_name} " + "{") or
                        tmp.endswith(f") *{struct_name} " + "{")):
                    tp0, tp1, tp2, tp3 = process_inputs(tmp.split("(")[1].split(")")[0],
                                                        structs_map, True)
                    rt = tmp.split("{")[0].split(")")[-1].strip()
                    structs_map[struct_name]["construct"] = (tmp.split("(")[0].split("func ")[-1].strip(),
                                                             (tp0, tp1, tp2, tp3.replace("values", "vals[0]")),
                                                             rt)
                elif tmp.startswith("func (") and struct_name in tmp.split(")")[0]:
                    if "funcs" not in structs_map[struct_name]:
                        structs_map[struct_name]["funcs"] = []
                    tp0, tp1, tp2, tp3 = process_inputs(tmp.split("(")[2].split(")")[0],
                                                        structs_map, True)
                    rt = tmp.split("{")[0].split(")")[-1].strip()
                    structs_map[struct_name]["funcs"].append((tmp.split("(")[1].split(")")[-1].strip(),
                                                              (tp0, tp1, tp2, tp3.replace("values", "vals[i]")),
                                                              rt))

            import_set = set()
            func_loop = ""
            constructor = None
            for d in structs_map.values():
                if "funcs" in d:
                    for name, its, rt in d["funcs"]:
                        import_set.update(its[0])
                        func_loop += ("\t\tcase \"{}\", \"{}\":\n"
                                      "\t\t\t{}obj.{}({})\n").format(name[0].lower() + name[1:], name,
                                                                     "res = nil\n\t\t\t" if rt == "" else "res = ",
                                                                     name, its[3])
                if "construct" in d:
                    constructor = d["construct"]
            build_body = ("\tvar opts []string\n" +
                          "\tvar vals [][]interface{}\n" +
                          "\tvar ans []interface{}\n" +
                          "\tif err := json.Unmarshal([]byte(values[0]), &opts); err != nil {\n" +
                          "\t\tlog.Println(err)\n" +
                          "\t\treturn nil\n" +
                          "\t}\n" +
                          "\tif err := json.Unmarshal([]byte(values[1]), &vals); err != nil {\n" +
                          "\t\tlog.Println(err)\n" +
                          "\t\treturn nil\n" +
                          "\t}\n" +
                          "{}".format(
                              "\tobj :=" + constructor[
                                  0] + f"({constructor[1][3]})\n" if constructor is not None else "",
                              ""
                          ) +
                          "\tans = append(ans, nil)\n" +
                          "\tfor i := 1; i < len(opts); i++ {\n" +
                          "\t\tvar res interface{}\n" +
                          "{}".format(
                              "\t\tswitch opts[i] {\n" +
                              func_loop +
                              "\t\tdefault:\n"
                              "\t\t\tres = nil\n"
                              "\t\t}\n"
                          ) +
                          "\t\tans = append(ans, res)\n"
                          "\t}\n"
                          )

            return base_str.format(
                problem_id,
                "\n".join(sorted(import_set, key=lambda x: "\t" + x.split(" ")[-1] if x.startswith('\t. ') else x)),
                code_default if default else code,
                "interface{} {",
                build_body,
                "",
                "ans",
                "",
                "}",
            ).replace("return ans()", "return ans")
    import_set = set()
    for it in its:
        import_set.update(it[0])

    if len(rts) != 1 or rts[0] == "*TreeNode" or rts[0] == "*ListNode" or rts[0] == "*Node":
        return_func_var = "{}({})".format(func_names[0],
                                          ", ".join(list(zip(*its))[3]))
        match rts[0]:
            case "*TreeNode":
                return_func_name = "TreeToArray"
            case "*ListNode":
                return_func_name = return_func_var + ".LinkedListToIntArray"
                return_func_var = ""
            case "*Node":
                return_func_name = "ToBeImplemented"
                if ("Left *Node" in code_default
                        and "Right *Node" in code_default
                        and "Next *Node" in code_default):
                    return_func_name = "TreeNextToArray"
                elif "Neighbors []*Node" in code_default:
                    return_func_name = "NodeNeighbourToArrayRelation"
                elif "/**\n" \
                     " * Definition for a Node.\n" \
                     " * type Node struct {\n" \
                     " *     Val int\n" \
                     " *     Next *Node\n" \
                     " *     Random *Node\n" \
                     " * }\n" \
                     " */" in code_default:
                    return_func_name = "NodeArrayToIntRandomArray"
            case _:
                return_func_name = ""

        return base_str.format(
            problem_id,
            # string with . starts before other, othercase sort normal
            "\n".join(sorted(import_set, key=lambda x: "\t" + x.split(" ")[-1] if x.startswith('\t. ') else x)),
            code_default if default else code,
            "interface{} {",
            "\n".join(list(zip(*its))[1]),
            "\n".join(list(zip(*its))[2]),
            return_func_name,
            return_func_var,
            "}",
        )
    return base_str.format(
        problem_id,
        "\n".join(sorted(import_set, key=lambda x: "\t" + x.split(" ")[-1] if x.startswith('\t. ') else x)),
        code_default if default else code,
        "interface{} {",
        "\n".join(list(zip(*its))[1]),
        "\n".join(list(zip(*its))[2]),
        func_names[0],
        ", ".join(list(zip(*its))[3]),
        "}",
    )
