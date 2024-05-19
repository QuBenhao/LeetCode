from python.constants import SOLUTION_TEMPLATE_JAVA


def change_test_java(content: str, question_id: str) -> str:
    ans = []
    for line in content.split("\n"):
        if "private static final String PROBLEM_ID = " in line:
            ans.append(line.split("\"")[0] + f"\"{question_id}\"")
            continue
        ans.append(line)
    return "\n".join(ans)


def __process_variable_type(input_name: str, variable_name: str, rt_type: str) -> str:
    match rt_type:
        case "int":
            return f"{rt_type} {variable_name} = Integer.parseInt({input_name});"
        case "int[]":
            return f"{rt_type} {variable_name} = jsonArrayToIntArray({input_name});"
        case "int[][]":
            pass
        case _:
            print("Not Implemented for {}".format(rt_type))
    return f"{rt_type} {variable_name} = notImplemented({input_name})"


def write_solution_java(code_default: str, code: str = None, problem_id: str = "") -> str:
    import_packages = []
    body = []
    parse_input = []
    return_part = ""
    import_part = True
    variables = []
    code = code if code else code_default
    for line in code.split("\n"):
        if "class Solution {" in line:
            import_part = False
            continue
        if import_part:
            import_packages.append(line)
        else:
            strip_line = line.strip()
            if strip_line.startswith("public ") and strip_line.endswith("{"):
                return_func = strip_line.split("(")[0].split(" ")[-1]
                # return_type = strip_line.split("(")[0].split(" ")[1]
                input_parts = strip_line.split("(")[1].split(")")[0].strip().split(",")
                for i, input_part in enumerate(input_parts):
                    var_split = input_part.strip().split(" ")
                    rt_type, variable = var_split[0], var_split[1]
                    variables.append(variable)
                    parse_input.append(__process_variable_type(f"values[{i}]", variable, rt_type))
                return_part = "{}({})".format(return_func, ",".join(variables))
            body.append(line)

    return SOLUTION_TEMPLATE_JAVA.format(
        problem_id,
        "\n".join(import_packages),
        "{",
        "\n".join(body),
        "{",
        "\n\t\t".join(parse_input),
        return_part,
        "}",
        "}"
    )
