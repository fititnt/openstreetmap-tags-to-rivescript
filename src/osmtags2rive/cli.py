import argparse
import json
import os
import sys
import osmtags2rive

# from osmtags2rive.osmtags2rive import WikiAsBase2Zip

EXIT_OK = 0  # pylint: disable=invalid-name
EXIT_ERROR = 1  # pylint: disable=invalid-name
EXIT_SYNTAX = 2  # pylint: disable=invalid-name


# Local install of cli (without upload).
#   python3 -m build
#   python3 -m pip install dist/osmtags2rive-0.2.1-py3-none-any.whl --force

# Examples
#   osmtags2rive --page-title 'User:EmericusPetro/sandbox/Wiki-as-base' | jq .data[1].data_raw
#   osmtags2rive --input-stdin < tests/data/multiple.wiki.txt | jq .data[1].data_raw
#   cat tests/data/multiple.wiki.txt | osmtags2rive --input-stdin | jq .data[1].data_raw


def main():

    parser = argparse.ArgumentParser(
        prog="osmtags2rive",
        description="Convert openstreetmap/id-tagging-schema to RiveScript",
    )

    # parser.add_argument(
    #     'integers', metavar='N', type=int, nargs='+',
    #     help='an integer for the accumulator')
    # parser.add_argument(
    #     '-greet', action='store_const', const=True,
    #     default=False, dest='greet',
    #     help="Greet Message from Geeks For Geeks.")
    # parser.add_argument(
    #     '--sum', dest='accumulate', action='store_const',
    #     const=sum, default=max,
    #     help='sum the integers (default: find the max)')

    # added --titles as aliases existing --page-title
    # parser.add_argument("--page-title", help="Page title of input")
    parser.add_argument(
        "--titles", "--page-title", help="Page titles of input, Use | as separator"
    )

    args = parser.parse_args()

    print(args)

    return EXIT_ERROR


if __name__ == "__main__":
    main()


def exec_from_console_scripts():
    main()
