import sys
from utils import send_text_message


def main():
    result = send_text_message("Hello World!")
    print(result)


if __name__ == '__main__':
    main()
    sys.exit()
