import argparse
import sys
import os
import shutil


def main(folder: str, force: bool = False) -> None:
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = os.path.join(root_path, folder)
    for root, dirs, files in os.walk(dir_path):
        for name in dirs:
            cur_path = os.path.join(dir_path, name)
            if not force and os.listdir(cur_path):
                print(f"skip problem[{name}]")
                continue
            shutil.rmtree(cur_path)
            print(f"remove problem[{name}]")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-dir", "--folder", required=True, type=str,
                        help="The folder to clean up.")
    parser.add_argument("-f", "--force", required=False, action="store_true",
                        help="Careful! If exists problem files before, it will still be cleaned!")
    args = parser.parse_args()
    main(args.folder, args.force)
    sys.exit()
