import os.path
from collections import defaultdict

from python.constants import SOLUTION_TEMPLATE_TYPESCRIPT

_LIST_NODE_PATH = "\"../../typescript/models/listnode\";"
_TREE_NODE_PATH = "\"../../typescript/models/treenode\";"


def change_test_typescript(content: str, question_id: str) -> str:
    pass


def write_solution_typescript(code_default: str, code: str = None, problem_id: str = "") -> str:
    import_part = defaultdict(set)
    code = code if code else code_default
    comment = False
    functions = []
    for line in code_default.split("\n"):
        strip_line = line.strip()
        if strip_line.startswith("/**"):
            comment = True
            continue
        if comment:
            if strip_line.endswith("*/"):
                comment = False
            continue
        if strip_line.startswith("function "):
            func_name = strip_line.split("(")[0].split("function ")[-1].strip()
            variables = list(map(str.strip, strip_line.split("(")[1].split(")")[0].split(",")))
            return_type = strip_line.split("{")[0].split(")")[-1].split(":")[-1].strip()
            functions.append((func_name, variables, return_type))

    if len(functions) == 1:
        process_inputs = []
        var_names = []
        func = functions[0]
        for i, variable in enumerate(func[1]):
            var_name = variable.split(":")[0]
            var_names.append(var_name)
            var_type = variable.split(":")[-1].strip()
            match var_type:
                case "ListNode | null":
                    import_part[_LIST_NODE_PATH].add("ListNode")
                    import_part[_LIST_NODE_PATH].add("IntArrayToLinkedList")
                    process_inputs.append(f"const {variable} = IntArrayToLinkedList(JSON.parse(splits[{i}]));")
                case "TreeNode | null":
                    import_part[_TREE_NODE_PATH].add("TreeNode")
                    import_part[_TREE_NODE_PATH].add("JSONArrayToTreeNode")
                    process_inputs.append(f"const {variable} = JSONArrayToTreeNode(JSON.parse(splits[{i}]));")
                case "Array<ListNode | null>":
                    import_part[_LIST_NODE_PATH].add("ListNode")
                    import_part[_LIST_NODE_PATH].add("IntArrayToLinkedList")
                    process_inputs.append(f"const jsonArray{i}: any = JSON.parse(splits[{i}]);")
                    process_inputs.append(f"const {variable} = [];")
                    process_inputs.append(f"for (let i = 0; i < jsonArray{i}.length; i++) " + "{")
                    process_inputs.append(f"\t{var_name}.push(IntArrayToLinkedList(jsonArray{i}[i]));")
                    process_inputs.append("}")
                case _:
                    process_inputs.append(f"const {variable} = JSON.parse(splits[{i}]);")
        match func[2]:
            case "ListNode | null":
                import_part[_LIST_NODE_PATH].add("ListNode")
                import_part[_LIST_NODE_PATH].add("LinkedListToIntArray")
                return_part = "LinkedListToIntArray({}({}))".format(func[0], ", ".join(var_names))
            case "TreeNode | null":
                import_part[_TREE_NODE_PATH].add("TreeNode")
                import_part[_TREE_NODE_PATH].add("TreeNodeToJSONArray")
                return_part = "TreeNodeToJSONArray({}({}))".format(func[0], ", ".join(var_names))
            case _:
                return_part = "{}({})".format(func[0], ", ".join(var_names))
        return SOLUTION_TEMPLATE_TYPESCRIPT.format(
            "" if not import_part else "\n".join(
                ["import {" + ",".join(v) + "} from " + k for k, v in import_part.items()]) + "\n\n",
            code,
            "{",
            "\t" + "\n\t".join(process_inputs),
            return_part,
            "}")
    return SOLUTION_TEMPLATE_TYPESCRIPT.format(
        "" if not import_part else "\n".join(
            ["import {" + ",".join(v) + "} from " + k for k, v in import_part.items()]) + "\n\n",
        code,
        "{",
        "\tprocess input",
        "return part",
        "}")


def get_solution_code_typescript(root_path, problem_folder: str, problem_id: str) -> (str, str):
    pass
