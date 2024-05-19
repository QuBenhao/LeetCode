import os
import subprocess
import sys


def rename_folder(root, folder) -> str:
    return root.split("/")[-1] + "_" + folder


def process_folder(dir_path):
    if not os.path.exists(dir_path):
        return
    rename_src_dst = []
    for root, dirs, _ in os.walk(dir_path):
        for d in list(dirs):
            if not all(c.isdigit() for c in d):
                continue
            src = os.path.join(root, d)
            dst = os.path.join(root, rename_folder(root, d))
            rename_src_dst.append((src, dst))
            dirs.remove(d)

    for src, dst in rename_src_dst:
        os.rename(src, dst)


def fix_java_files(dir_path):
    if not os.path.exists(dir_path):
        return
    for root, dirs, files in os.walk(dir_path):
        # if not files:
        #     continue
        # package_path = ".".join(root.split("/")[-2:])
        for f in files:
            if not f.endswith(".java"):
                continue
            print(f)
            # with open(os.path.join(root, f), 'r', encoding="utf-8") as file:
            #     lines = file.readlines()
            # if "package" not in lines[0]:
            #     lines = [f"package {package_path};\n\n"] + lines
            # for i, l in enumerate(lines):
            #     if "class Solution" in l and "public" not in l:
            #         lines[i] = "public " + l
            # with open(os.path.join(root, f), 'w', encoding="utf-8") as file:
            #     file.writelines(lines)
            if f[0].isupper():
                continue
            res = subprocess.run(
                ["git", "mv", str(os.path.join(root, f)), os.path.join(root, str(f[0].upper()) + "".join(f[1:]))])
            print(res)
            # os.rename(src=str(os.path.join(root, f)), dst=str(os.path.join(root, str(f[0].upper()) + "".join(f[1:]))))


def main(problem_folders: set[str]):
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    for folder in problem_folders:
        dir_path = os.path.join(root_path, folder)
        # process_folder(dir_path)
        fix_java_files(dir_path)


if __name__ == '__main__':
    main({"problems", "premiums", "mysql"})
    sys.exit()
