#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  osmtags2rive.py
#
#         USAGE:  ---
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  ---
#       CREATED:  ---
# ==============================================================================

# import copy
# from abc import ABC
# import csv

# import datetime
# import io
# import json
# import os
# import re
# import sys

# import sys
# from typing import Any, List, Union
# from typing import List
# import zipfile
# import requests
# import requests_cache


class OSMTags2Rive:

    language: str
    id_tagging_schema_path: str
    _out: str

    def __init__(self, language: str, ref_path) -> None:

        self.language = language
        self.id_tagging_schema_path = ref_path

        self._init_memory()

        # pass

    def _init_memory(self):

        with open(
            self.id_tagging_schema_path
            + "/dist/translations/"
            + self.language
            + ".json",
            "r",
        ) as _file:
            self._out = _file.read()
        # pass

    def output(self) -> str:

        return self._out
