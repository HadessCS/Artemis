import argparse

import pyftype


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("p", help="path")
    parser.add_argument(
        "-V", "--version", action="version", version=pyftype.__version__
    )

    args = parser.parse_args()
    kind = pyftype.guess(args.p)
    print("File extension: {}".format(kind.extension))
    print("File MIME type: {}".format(kind.mime))


if __name__ == "__main__":
    main()
