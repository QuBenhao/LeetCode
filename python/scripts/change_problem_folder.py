import os
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

def main(problem_folders: set[str]):
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    for folder in problem_folders:
        process_folder(os.path.join(root_path, folder))


if __name__ == '__main__':
    main({"problems", "premiums", "mysql"})
    sys.exit()
