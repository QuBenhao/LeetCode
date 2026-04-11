import os, json

def parse_env(path):
    d = {}
    if os.path.exists(path):
        for line in open(path):
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                d[k.strip()] = v.strip().strip('"').strip("'")
    return d

def resolve_link(problem_path, visited=None, original_link_info=None):
    """Resolve problem link if link.json exists. Returns (resolved_path, link_info)."""
    if visited is None:
        visited = set()

    link_file = os.path.join(problem_path, "link.json")
    if not os.path.exists(link_file):
        return problem_path, original_link_info

    problem_id = os.path.basename(problem_path).split("_")[-1]
    if problem_id in visited:
        raise ValueError(f"Circular link detected involving problem {problem_id}")
    visited.add(problem_id)

    with open(link_file, 'r') as f:
        link_info = json.load(f)

    # Keep the first link_info encountered
    if original_link_info is None:
        original_link_info = link_info

    link_to = link_info["link_to"]
    link_folder = link_info.get("link_folder", "problems")
    base_path = os.path.join(os.path.dirname(problem_path), f"{link_folder}_{link_to}")

    return resolve_link(base_path, visited, original_link_info)

root = os.path.dirname(__file__)
env = parse_env(os.path.join(root, ".env"))
folder = env.get("PROBLEM_FOLDER", "problems")
json_path = os.path.join(root, f"daily-{folder}.json")
with open(json_path) as f:
    data_json = json.load(f)
    daily = data_json.get("daily", "1")
    plans = data_json.get("plans", [])

# Collect link mappings for Bazel
link_mappings = {}

def collect_link_mapping(problem_id, problem_folder):
    problem_path = os.path.join(root, problem_folder, f"{problem_folder}_{problem_id}")
    resolved_path, link_info = resolve_link(problem_path)
    if link_info:
        linked_id = os.path.basename(resolved_path).split("_")[-1]
        linked_folder = os.path.basename(os.path.dirname(resolved_path))
        link_mappings[f"{problem_folder}_{problem_id}"] = f"{linked_folder}_{linked_id}"
        return linked_folder, linked_id
    return problem_folder, problem_id

# Collect for daily
collect_link_mapping(daily, folder)

# Collect for plans
for i in range(0, len(plans), 2):
    plan_id = plans[i]
    plan_folder = plans[i + 1]
    collect_link_mapping(plan_id, plan_folder)

# Output for Bazel
print(folder)
print(daily)
print(",".join(plans))

# Generate link_mappings.bzl for Bazel to use
if link_mappings:
    bzl_content = "# Auto-generated link mappings\nLINK_MAPPINGS = {\n"
    for k, v in link_mappings.items():
        bzl_content += f'    "{k}": "{v}",\n'
    bzl_content += "}\n"

    bzl_path = os.path.join(root, "link_mappings.bzl")
    with open(bzl_path, 'w') as f:
        f.write(bzl_content)
    print(f"Generated: {bzl_path}")
