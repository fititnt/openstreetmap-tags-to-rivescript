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


import json


class OSMTags2Rive:

    language: str
    id_tagging_schema_path: str
    _source: str
    _source_presets: dict
    _rive: list

    def __init__(self, language: str, ref_path) -> None:

        self.language = language
        self.id_tagging_schema_path = ref_path

        self._init_memory()
        self._init_rive()

        # pass

    def _init_memory(self) -> bool:

        with open(
            self.id_tagging_schema_path
            + "/dist/translations/"
            + self.language
            + ".json",
            "r",
        ) as _file:
            self._source = _file.read()

            _source = json.loads(self._source)
            self._source_presets = _source[self.language]["presets"]
        return True

    def _init_rive(self) -> bool:
        self._rive = [
            "// openstreetmap/id-tagging-schema " + self.language,
            "",
            "! version = 2.0",
            "",
        ]

        self._rive.append("")
        self._rive.append("// *** fields ***/")
        for field_key, field_val in self._source_presets["fields"].items():
            trigger = self._sanitize_trigger(field_key)

            self._rive.append("")
            self._rive.append(f"+ {trigger}")
            self._rive.append(f'- {field_val["label"]}')

        self._rive.append("")
        self._rive.append("// *** presets ***/")
        for field_key, field_val in self._source_presets["presets"].items():
            
            trigger = self._sanitize_trigger(field_key)
            self._rive.append("")
            self._rive.append(f"+ {trigger}")
            self._rive.append(f'- {field_val["name"]}')

        return True

    def _sanitize_trigger(self, trigger: str) -> str:
        trigger_norm = trigger.replace("/", " ").replace("-", " ").replace("_", " ")
        trigger_norm = trigger_norm.lower()
        return trigger_norm

    def output(self) -> str:

        return "\n".join(self._rive)

    def output_source(self) -> str:

        return self._source
