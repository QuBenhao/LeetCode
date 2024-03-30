import inspect
import os
import traceback
from collections import defaultdict
from importlib.util import spec_from_file_location, module_from_spec
from typing import Union


def write_problem_md(question_id: str, question_name: str, desc: str) -> str:
    return "# {}. {}\n\n{}".format(question_id, question_name, desc)


def write_testcase(testcases, outputs) -> str:
    res = ""
    res += 'from collections import namedtuple\n'
    res += 'import testcase\n\n'
    res += 'case = namedtuple("Testcase", ["Input", "Output"])\n\n\n'
    res += 'class Testcase(testcase.Testcase):\n'
    res += '\tdef __init__(self):\n'
    res += '\t\tself.testcases = []\n'
    for inputs, output in zip(testcases, outputs):
        res += ('\t\tself.testcases.append(case(Input={}, Output={}))\n'
                .format(f"\"{output}\"" if isinstance(inputs, str) else inputs,
                        f"\"{output}\"" if isinstance(output, str) else output))
    res += '\n\tdef get_testcases(self):\n'
    res += '\t\treturn self.testcases\n'
    return res


def __process_code__(code: str):
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
        # Get the method of your class
        methods = inspect.getmembers(cs[1], inspect.isroutine)

        # Filter out in-built dunder methods
        non_dunder_methods = [
            m for m in methods
            if (cs[0] != 'Solution' and m[0] == "__init__") or not (m[0].startswith('__') and m[0].endswith('__'))]

        for method in non_dunder_methods:
            md = getattr(cs[1], method[0])
            sig = inspect.signature(md)
            cs_map[cs[0]].append((method[0], dict(sig.parameters), sig.return_annotation))

    os.remove("tmp.py")
    return cs_map, top, res


def __finalize_solution_code__(cs_map, top, res):
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
                process_input = "return self.{}({})".format(methods[0][0], init_params)
        else:
            class_name, methods = "", []
            for k, v in cs_map.items():
                class_name, methods = k, v
            top[0] = top[0] + "from object_libs import call_method\n"
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
                        add_lib = "from object_libs import list_to_tree"
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
                        add_lib = "from object_libs import list_to_linked_list"
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
                    add_lib += ", tree_to_list" if exists else "from object_libs import tree_to_list"
                    remain += "        res = self.{}({})\n        return tree_to_list(res)".format(methods[0][0],
                                                                                                   inputs)
                elif "ListNode" in str(return_anno):
                    add_lib += ", linked_list_to_list" if exists else "from object_libs import linked_list_to_list"
                    remain += "        res = self.{}({})\n        return linked_list_to_list(res)".format(methods[0][0],
                                                                                                          inputs)
                else:
                    remain += "        return self.{}({})".format(methods[0][0], inputs)
                top[0] = top[0] + add_lib + "\n"

                process_input += remain
        else:
            top[0] = top[0] + "from object_libs import call_method"
            if "TreeNode" in cs_map:
                top[0] += ", list_to_tree"
                cs_map.pop("TreeNode")
            elif "ListNode" in cs_map:
                top[0] += ", linked_list_to_list"
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
                            else:
                                process_input += ", "
                                inputs += ", "
                            if "TreeNode" in str(v.annotation):
                                if "List[" in str(v.annotation):
                                    process_input += "        nums_arr"
                                    remain += "        roots = [list_to_tree(nums) for nums in nums_arr]\n"
                                    inputs += "roots"
                                else:
                                    process_input += f"        nums{idx}"
                                    remain += f"        root{idx} = list_to_tree(nums{idx})\n"
                                    inputs += f"root{idx}"
                                    idx += 1
                            elif "ListNode" in str(v.annotation):
                                if "List[" in str(v.annotation):
                                    process_input += "        nums_arr"
                                    remain += f"        heads = [list_to_linked_list(nums) for nums in nums_arr]\n"
                                    inputs += "heads"
                                else:
                                    process_input += f"        nums{idx}"
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


def write_solution(code: str, default: bool = True) -> str:
    if not default:
        if "class Solution" in code:
            return "\n".join(code.split("class Solution")[-1].split("\n")[1:])
        return code
    try:
        cs_map, top, res = __process_code__(code)
        top, res = __finalize_solution_code__(cs_map, top, res)

        return "\n".join(top) + "\n\n" + "\n".join(res)
    except Exception as e:
        print("Exception raised:", e)
        traceback.print_exc()
        if os.path.exists("tmp.py"):
            os.remove("tmp.py")

    if '"""' in code:
        sp = code.split('"""')
        define_class = []
        code_source = ""
        for i in range(1, len(sp), 2):
            define_class.append(sp[i])
        for i in range(0, len(sp), 2):
            code_source += sp[i]
        strip_code = []
        for line in code_source.split("\n"):
            if line.startswith("from typing import"):
                continue
            if line.startswith("class Solution"):
                continue
            if len(line) > 0:
                strip_code.append(line)
        return ("import solution\n"
                "from typing import *\n\n"
                "{}"
                "class Solution(solution.Solution):\n"
                "    def solve(self, test_input=None):\n"
                "        pass\n\n"
                "{}").format("".join(define_class) + "\n\n" if define_class else "\n", "\n".join(strip_code))
    if "class Solution" in code or "# class" in code:
        start = False
        strip_start = False
        strip_code = []
        define_class = []
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
        return ("import solution\n"
                "from typing import *\n\n\n"
                "{}"
                "class Solution(solution.Solution):\n"
                "    def solve(self, test_input=None):\n"
                "        pass\n\n"
                "{}").format("\n".join(define_class) + "\n\n\n" if define_class else "", "\n".join(strip_code))
    return ("import solution\n"
            "from typing import *\n\n\n"
            "class Solution(solution.Solution):\n"
            "    def solve(self, test_input=None):\n"
            "        pass\n\n\n"
            "{}\n").format(code)
