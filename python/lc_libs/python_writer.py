import inspect
import logging
import os
import time
import traceback
from typing import Tuple
from collections import defaultdict, deque
from importlib.util import spec_from_file_location, module_from_spec

from python.constants import TESTCASE_TEMPLATE_PYTHON, TESTCASE_TEMPLATE_PYTHON_TESTCASES, SOLUTION_TEMPLATE_PYTHON
from python.lc_libs.language_writer import LanguageWriter
from python.utils import back_question_id


class Python3Writer(LanguageWriter):

    def __init__(self) -> None:
        super().__init__()
        self.solution_file = "solution.py"
        self.main_folder = "python"
        self.test_file = "test.py"
        self.tests_file = "tests.py"
        self.lang_env_commands = [["python", "--version"]]
        self.test_commands = [["python", os.path.join(self.main_folder, self.test_file)]]

    def change_test(self, root_path, problem_folder: str, question_id: str):
        file_path = os.path.join(root_path, self.main_folder, self.test_file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        with open(file_path, "w", encoding="utf-8") as f:
            lines = content.split("\n")
            for line_idx, line in enumerate(lines):
                if line.startswith("QUESTION = "):
                    f.write(f'QUESTION = "{question_id}"\n')
                    continue
                if line_idx < len(lines) - 1 or line:
                    f.write(line + "\n")

    def change_tests(self, root_path, problem_ids_folders: list):
        file_path = os.path.join(root_path, self.main_folder, self.tests_file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        with open(file_path, "w", encoding="utf-8") as f:
            lines = content.split("\n")
            for line_idx, line in enumerate(lines):
                if line.startswith("QUESTIONS ="):
                    line = "QUESTIONS = {}".format(problem_ids_folders)
                if line_idx < len(lines) - 1 or line:
                    f.write(line + "\n")

    def write_solution(self, code_template: str, code: str = None, problem_id: str = "",
                       problem_folder: str = "") -> str:
        try:
            cs_map, defined_class, rest = Python3Writer.__process_code(code_template)
            modify_in_place = "Do not return anything" in code_template
            if len(cs_map) == 1:
                import_libs, process_input = (Python3Writer.
                                              __finalize_solution_code_with_single_class(cs_map, modify_in_place))
            else:
                testcases = LanguageWriter.get_test_cases(problem_folder, problem_id)
                import_libs, process_input = Python3Writer.__finalize_solution_code_complex(
                    cs_map, modify_in_place, testcases)
            if code:
                # submission code, not template code
                if "class Solution" in code:
                    last_part = "\n".join(code.split("class Solution")[-1].split("\n")[1:])
                else:
                    last_part = code
            else:
                last_part = ("" if not rest or "(self" in rest[0] else "\n") + "\n".join(rest)
            return SOLUTION_TEMPLATE_PYTHON.format(
                "".join(import_libs) + ("\n" if import_libs and defined_class else "") +
                (("\n" if defined_class else "") + "\n".join(defined_class) + ("\n" if defined_class else "")),
                process_input,
                last_part
            )
        except Exception as _:
            logging.error(f"Failed to write [{problem_id}] python3 solution", exc_info=True)
        logging.warning("Fall back to write python3 backup solution")
        return Python3Writer.__write_solution_python_backup(code_template)

    def get_solution_code(self, root_path, problem_folder: str, problem_id: str) -> Tuple[str, str]:
        if not problem_id:
            with open(os.path.join(root_path, self.main_folder, self.test_file), "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip().startswith("QUESTION ="):
                        problem_id = line.split("=")[-1].strip().replace('"', '')
                        break
        if not problem_id:
            return "", problem_id
        file_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{problem_id}", "solution.py")
        if not os.path.exists(file_path):
            return "", problem_id
        final_codes = []
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            skip_solution = "from python.object_libs import " in content and " call_method" in content
            idx = content.find("def solve(self, test_input=None):")
            idx = content.find("return ", idx)
            idx = content.find("\n", idx) + 1
            while idx < len(content) and content[idx] == "\n":
                idx += 1
            logging.debug("Start idx: %d", idx)
            if not skip_solution:
                final_codes.append("class Solution:")
            final_codes.extend(content[idx:].split("\n"))
        return "\n".join(final_codes), problem_id

    @staticmethod
    def write_problem_md(question_id: str, question_name: str, desc: str, cn: bool = False,
                         rating: float = None) -> str:
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
        return "# {}. {} {}\n\n{}".format(back_question_id(question_id), question_name,
                                          "" if not rating else "[{}: {:.2f}]".format(
                                              "难度分" if cn else "Rating", rating),
                                          "\n".join(formated))

    @staticmethod
    def write_testcase(testcases, outputs) -> str:
        if len(testcases) == 0 or len(outputs) == 0:
            logging.error("No testcases or outputs found, please check the problem."
                          " Testcases: %s, Outputs: %s", testcases, outputs)
        elif len(testcases) != len(outputs):
            logging.warning("Testcases [%d] and outputs [%d] are not the same length, "
                            "please check the testcases and outputs", len(testcases), len(outputs))
        res = ""
        for inputs, output in zip(testcases, outputs):
            res += (TESTCASE_TEMPLATE_PYTHON_TESTCASES
                    .format(f"\"{inputs}\"" if isinstance(inputs, str) else inputs,
                            f"\"{output}\"" if isinstance(output, str) else output))
        return TESTCASE_TEMPLATE_PYTHON.format(res)

    @staticmethod
    def __get_code_class(tmp_filename):
        include_solution_class = False
        solution_spec = spec_from_file_location("module.name", tmp_filename)
        solution = module_from_spec(solution_spec)
        solution_spec.loader.exec_module(solution)
        classes = inspect.getmembers(solution, inspect.isclass)
        your_classes = [c for c in classes if c[1].__module__ == solution.__name__]

        cs_map = defaultdict(list)
        for cs in your_classes:
            class_name = cs[0]
            # Get the method of your class
            methods = inspect.getmembers(cs[1], inspect.isroutine)

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
                    include_solution_class = True
                cs_map[class_name].append((method[0], dict(sig.parameters), sig.return_annotation))

        return cs_map, include_solution_class

    @staticmethod
    def __process_code(code: str):
        class_defines = []
        rest = []
        process_class = False
        splits = code.split("\n")
        idx = 0
        while idx < len(splits):
            line = splits[idx]
            if "# class " in line:
                process_class = True
                class_defines.append(line[2:])
                idx += 1
                continue
            elif process_class:
                if line.startswith("#"):
                    class_defines.append(line[2:])
                    idx += 1
                    continue
                else:
                    process_class = False
            if ('"""' in line and idx < len(splits) - 1 and
                    (splits[idx + 1].strip().startswith("class ") or splits[idx + 1].strip().startswith("# "))):
                idx += 1
                while idx < len(splits) and '"""' not in splits[idx]:
                    if "from typing import " not in rest:
                        class_defines.append(splits[idx])
                    idx += 1
                idx += 1
                continue
            if "from typing import " in line:
                idx += 1
                continue
            sl = line.strip()
            if sl and not sl.startswith("#"):
                rest.append(line)
            if sl.startswith("def ") and sl.endswith(":"):
                if idx < len(splits) - 1 and '"""' in splits[idx + 1]:
                    idx += 1
                    while idx < len(splits) - 1 and '"""' not in splits[idx + 1].strip():
                        rest.append(splits[idx])
                        idx += 1
                    rest.append(splits[idx])
                    idx += 1
                    rest.append(splits[idx])
                    sp = splits[idx].count(" ", None, splits[idx].index('"""'))
                    sp = ((sp + 3) // 4) * 4
                else:
                    sp = line.count(" ", line.index("def "))
                    sp = ((sp + 3) // 4) * 4 + 4
                rest.append(sp * " " + "pass")
                rest.append("")
            idx += 1
        tmp_filename = "tmp-{}.py".format(time.time())
        try:
            with open(tmp_filename, "w", encoding="utf-8") as f:
                f.writelines("from typing import *\n\n")
                f.writelines("\n".join(class_defines) + "\n\n")
                f.writelines("\n".join(rest))
            cs_map, include_solution = Python3Writer.__get_code_class(tmp_filename)
            if include_solution:
                for i, line in enumerate(rest):
                    if "class Solution" in line:
                        rest[i] = line.replace("Solution", "S")
            simply = []
            last_space = 0
            in_comment = 0
            for line in rest:
                if "class Solution" in line:
                    continue
                strip_line = line.strip()
                if strip_line.startswith('"""'):
                    in_comment ^= 1
                    simply.append(line)
                    continue
                if line.strip() == "pass":
                    simply.append(" " * (last_space + 4) + "pass")
                else:
                    simply.append(line)
                    if not in_comment:
                        last_space = len(line) - len(line.lstrip())
            rest = simply
        finally:
            if os.path.exists(tmp_filename):
                os.remove(tmp_filename)
        return cs_map, class_defines, rest

    @staticmethod
    def __calculate_parameters(parameters):
        count = len(parameters)
        if "self" in parameters:
            count -= 1
        if "args" in parameters:
            count -= 1
        if "kwargs" in parameters:
            count -= 1
        return count

    @staticmethod
    def __extract_process_input_from_method(cs_map, modify_in_place, import_libs, method, testcases=None):
        func_name, parameters, return_anno = method
        par_map = dict()
        add_lib = ""
        exists = False
        process_input = ""
        remain = ""
        inputs = ""
        modify_in_place_inputs = ""
        is_first = True
        for k in list(parameters.keys()):
            if parameters[k].name == "self":
                parameters.pop(k)
            elif parameters[k].name == "args":
                parameters.pop(k)
            elif parameters[k].name == "kwargs":
                parameters.pop(k)
        idx = 0
        p_values = list(parameters.values())
        for vid, v in enumerate(p_values):
            if vid < idx:
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
                    if modify_in_place and not modify_in_place_inputs:
                        add_lib += ", tree_to_list" if exists else "from python.object_libs import tree_to_list"
                        modify_in_place_inputs = "tree_to_list(roots[0])"
                else:
                    if testcases:
                        if (len(p_values) == len(testcases[0]) + 1 and
                                all("TreeNode" in str(p.annotation) for p in p_values)):
                            process_input += f"nums{idx}, target_val"
                            remain += (f"        original, target = list_to_tree_with_target(nums{idx},"
                                       f" target_val)\n")
                            remain += f"        cloned = list_to_tree(nums0)\n"
                            inputs += f"original, cloned, target"
                            idx += 3
                            continue
                        i = idx + 1
                        while all(i < len(testcase)
                                  and "TreeNode" in str(p_values[i].annotation)
                                  and testcase[i] is not None
                                  and not isinstance(testcase[i], list) for testcase in testcases):
                            i += 1
                        if i != idx + 1:
                            add_lib += ", list_to_tree_with_target"
                            process_input += f"nums{idx}"
                            for j in range(idx + 1, i):
                                process_input += f", num{j}"
                            remain += f"        nodes = list_to_tree_with_target(nums{idx}, " + ", ".join(
                                [f"num{j}" for j in range(idx + 1, i)]) + ")\n"
                            remain += f"        root{idx} = nodes[0]\n"
                            for j in range(idx + 1, i):
                                remain += f"        node{j} = nodes[{j - idx}]\n"
                            inputs += f"root{idx}, " + ", ".join([f"node{j}" for j in range(idx + 1, i)])
                            idx = i
                            continue
                    process_input += f"nums{idx}"
                    remain += f"        root{idx} = list_to_tree(nums{idx})\n"
                    inputs += f"root{idx}"
                    if modify_in_place and not modify_in_place_inputs:
                        add_lib += ", tree_to_list" if exists else "from python.object_libs import tree_to_list"
                        modify_in_place_inputs = f"tree_to_list(root{idx})"
                    idx += 1
            elif "ListNode" in str(v.annotation):
                exists = True
                add_lib = "from python.object_libs import list_to_linked_list"
                if "List[" in str(v.annotation):
                    process_input += "nums_arr"
                    remain += f"        heads = [list_to_linked_list(nums) for nums in nums_arr]\n"
                    inputs += "heads"
                    if modify_in_place and not modify_in_place_inputs:
                        add_lib += ", tree_to_list" if exists else "from python.object_libs import linked_list_to_list"
                        modify_in_place_inputs = "linked_list_to_list(heads[0])"
                else:
                    if testcases:
                        if len(testcases[0]) == len(p_values) + 1 and all(
                                isinstance(testcase[0], list)
                                and isinstance(testcase[1], int)
                                for testcase in testcases):
                            add_lib += ", list_to_linked_list_cycle"
                            process_input += f"nums{idx}, pos{idx}"
                            remain += f"        head{idx} = list_to_linked_list_cycle(nums{idx}, pos{idx})\n"
                            inputs += f"head{idx}"
                            idx += 2
                            logging.debug(process_input)
                            continue
                        elif (len(p_values) == 2 and all("ListNode" in str(p.annotation) for p in p_values) and
                              len(testcases[0]) == 5 and all(isinstance(testcase[0], int) and
                                                             isinstance(testcase[1], list) and
                                                             isinstance(testcase[2], list) and
                                                             isinstance(testcase[3], int) and
                                                             isinstance(testcase[4], int) for testcase in testcases)):
                            add_lib += ", list_to_linked_list_intersection"
                            process_input += "iv, nums1, nums2, idx1, idx2"
                            remain += ("        head1, head2 = "
                                       "list_to_linked_list_intersection(iv, nums1, nums2, idx1, idx2)\n")
                            inputs += "head1, head2"
                            idx += 5
                            continue
                        elif len(p_values) != len(testcases[0]):
                            logging.debug(f"Testcases: {testcases}, p_values: {p_values}")
                    process_input += f"nums{idx}"
                    remain += f"        head{idx} = list_to_linked_list(nums{idx})\n"
                    inputs += f"head{idx}"
                    if modify_in_place and not modify_in_place_inputs:
                        add_lib += ", tree_to_list" if exists else "from python.object_libs import linked_list_to_list"
                        modify_in_place_inputs = f"linked_list_to_list(head{idx})"
                    idx += 1
            elif "Node" in str(v.annotation) and "Node" in cs_map and "neighbors" in cs_map["Node"][0][1]:
                # special handle Neighbour Nodes
                exists = True
                add_lib = "from python.object_libs import list_relation_to_node_neigh"
                if "List[" in str(v.annotation):
                    process_input += "nums_arr"
                    remain += f"        roots = [list_relation_to_node_neigh(nums) for nums in nums_arr]\n"
                    inputs += "roots"
                else:
                    process_input += f"nums{idx}"
                    remain += f"        node{idx} = list_relation_to_node_neigh(nums{idx})\n"
                    inputs += f"node{idx}"
            elif ("Node" in str(v.annotation) and "Node" in cs_map and "left" in cs_map["Node"][0][1] and
                  "right" in cs_map["Node"][0][1] and "next" in cs_map["Node"][0][1]):
                # special handle Next Nodes
                exists = True
                add_lib = "from python.object_libs import list_to_tree_next_node"
                process_input += "nums"
                remain += "        root = list_to_tree_next_node(nums)\n"
                inputs += "root"
            elif ("Node" in str(v.annotation) and "Node" in cs_map and "next" in cs_map["Node"][0][1] and
                  "random" in cs_map["Node"][0][1]):
                exists = True
                add_lib = "from python.object_libs import list_to_linked_random_list"
                process_input += "nums"
                remain += "        head = list_to_linked_random_list(nums)\n"
                inputs += "head"
            else:
                process_input += v.name
                inputs += v.name
                if modify_in_place and not modify_in_place_inputs:
                    modify_in_place_inputs = v.name
                idx += 1

        if len(parameters) > 0:
            process_input += " = test_input\n"

        if "TreeNode" in str(return_anno):
            add_lib += ", tree_to_list" if exists else "from python.object_libs import tree_to_list"
            if "List[" in str(return_anno):
                remain += ("        res = self.{}({})\n        return [tree_to_list(root) for root in res]"
                           .format(func_name, inputs))
            else:
                remain += ("        res = self.{}({})\n        return tree_to_list(res)"
                           .format(func_name, inputs))
        elif "ListNode" in str(return_anno):
            if "list_to_linked_list_cycle" in add_lib:
                logging.debug("Cycle linked list return")
                remain += ("        res = self.{}({})\n        return res.val if res else None"
                           .format(func_name, inputs))
            else:
                add_lib += ", linked_list_to_list" if exists else \
                    "from python.object_libs import linked_list_to_list"
                if "List[" in str(return_anno):
                    remain += ("res = self.{}({})\n        return [linked_list_to_list(head) for head in "
                               "res]").format(func_name, inputs)
                else:
                    remain += ("        res = self.{}({})\n        return linked_list_to_list(res)"
                               .format(func_name, inputs))
            logging.debug(remain)
        elif "Node" in str(return_anno) and "Node" in cs_map and "neighbors" in cs_map["Node"][0][1]:
            # special handle Neighbour Nodes
            add_lib += ", node_neigh_to_list_relation" if exists else \
                "from python.object_libs import node_neigh_to_list_relation"
            if "List[" in str(return_anno):
                remain += ("        res = self.{}({})\n"
                           "        return [node_neigh_to_list_relation(root) for root in res]"
                           .format(func_name, inputs))
            else:
                remain += ("        res = self.{}({})\n        return node_neigh_to_list_relation(res)"
                           .format(func_name, inputs))
        elif ("Node" in str(return_anno) and "Node" in cs_map and "left" in cs_map["Node"][0][1] and
              "right" in cs_map["Node"][0][1] and "next" in cs_map["Node"][0][1]):
            add_lib += ", tree_next_node_to_list" if exists else \
                "from python.object_libs import tree_next_node_to_list"
            remain += ("        res = self.{}({})\n        return tree_next_node_to_list(res)"
                       .format(func_name, inputs))
        elif ("Node" in str(return_anno) and "Node" in cs_map and "next" in cs_map["Node"][0][1] and
              "random" in cs_map["Node"][0][1]):
            add_lib += ", linked_random_list_to_list" if exists else \
                "from python.object_libs import linked_random_list_to_list"
            remain += ("        res = self.{}({})\n        return linked_random_list_to_list(res)"
                       .format(func_name, inputs))
        else:
            if not modify_in_place:
                remain += "        return self.{}({})".format(func_name, inputs)
            else:
                logging.debug("Modify in place complex: func_name [%s], inputs [%s], ", func_name, inputs)
                remain += "        self.{}({})\n        return {}".format(func_name, inputs, modify_in_place_inputs)
        import_libs.append(add_lib + "\n")

        process_input += remain
        return process_input

    @staticmethod
    def __extract_object_process_input_from_method(class_name, method):
        parameters = method[1]
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
        return process_input

    @staticmethod
    def __finalize_solution_code_with_single_class(cs_map, modify_in_place: bool = False):
        process_input = "pass"
        import_libs = []
        if "Solution" in cs_map:
            methods = cs_map["Solution"]
            if len(methods) == 1:
                parameters, return_anno = methods[0][1], methods[0][2]
                count = Python3Writer.__calculate_parameters(parameters)
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
            import_libs.append("from python.object_libs import call_method\n")
            init_params = ""
            for method in methods:
                if method[0] == "__init__":
                    parameters, return_anno = methods[0][1], methods[0][2]
                    count = Python3Writer.__calculate_parameters(parameters)
                    if count > 0:
                        init_params = "*inputs[0]"
                    break

            process_input = (("ops, inputs = test_input\n        obj = {}({})\n        return [None] + "
                              "[call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]")
                             .format(class_name, init_params))
        return import_libs, process_input

    @staticmethod
    def __finalize_solution_code_complex(cs_map, modify_in_place: bool = False, testcases=None):
        process_input = "pass"
        import_libs = []
        if "Solution" in cs_map:
            methods = cs_map["Solution"]
            if len(methods) == 1:
                process_input = Python3Writer.__extract_process_input_from_method(
                    cs_map, modify_in_place, import_libs, methods[0], testcases)
        else:
            import_libs.append("from python.object_libs import call_method")
            if "TreeNode" in cs_map:
                import_libs.append(", list_to_tree")
                cs_map.pop("TreeNode")
            elif "ListNode" in cs_map:
                import_libs.append(", list_to_linked_list")
                cs_map.pop("ListNode")
            else:
                # Too complex to fix here
                pass
            import_libs.append("\n")
            if len(cs_map) == 1:
                class_name, methods = "", []
                for k, v in cs_map.items():
                    class_name, methods = k, v
                for method in methods:
                    if method[0] == "__init__":
                        process_input = Python3Writer.__extract_object_process_input_from_method(class_name, method)
                        break

                process_input += ("        return [None] + [call_method(obj, op, *ipt)"
                                  " for op, ipt in zip(ops[1:], inputs[1:])]")

        return import_libs, process_input

    @staticmethod
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
