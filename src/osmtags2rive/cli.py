import argparse
import json
import os
import sys
from osmtags2rive import OSMTags2Rive, OSMTagsReverse2Rive


from .constants import ID_TAGGING_SCHEMA

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

    parser.add_argument(
        "--language",
        help="Output language. Example: pt",
        default="pt",
    )

    parser.add_argument(
        "--path-id-tagging-schema",
        help="Path to a directory with id-tagging-schema",
        default="./id-tagging-schema",
    )

    parser.add_argument(
        "--reverse-index",
        help="Generate inverse index (keywors to tags)",
        action="store_true",
    )

    args = parser.parse_args()

    if args.reverse_index:
        o2r = OSMTagsReverse2Rive(
            language=args.language, ref_path=args.path_id_tagging_schema
        )
    else:
        o2r = OSMTags2Rive(language=args.language, ref_path=args.path_id_tagging_schema)

    # print(args)
    print(o2r.output())

    return EXIT_ERROR


if __name__ == "__main__":
    main()


def exec_from_console_scripts():
    main()
