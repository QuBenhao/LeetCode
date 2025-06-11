import os, json

def parse_env(path):
    d = {}
    if os.path.exists(path):
        for line in open(path):
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                d[k.strip()] = v.strip().strip('"').strip("'")
    return d

root = os.path.dirname(__file__)
env = parse_env(os.path.join(root, ".env"))
folder = env.get("PROBLEM_FOLDER", "problems")
json_path = os.path.join(root, f"daily-{folder}.json")
with open(json_path) as f:
    data_json = json.load(f)
    daily = data_json.get("daily", "1")
    plans = data_json.get("plans", [])
print(folder)
print(daily)
print(",".join(plans))
