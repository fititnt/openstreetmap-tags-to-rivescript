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
from abc import ABC
import csv

# from ctypes import Union
import datetime
import io
import json
import os
import re
import sys

# import sys
# from typing import Any, List, Union
from typing import List
import zipfile
import requests
import requests_cache


_REFVER = "0.5.6"

USER_AGENT = os.getenv("USER_AGENT", "wiki-as-base/" + _REFVER)
WIKI_API = os.getenv("WIKI_API", "https://wiki.openstreetmap.org/w/api.php")

# Consider using prefix like https://dumps.wikimedia.org/backup-index.html
WIKI_NS = os.getenv("WIKI_NS", "osmwiki")
WIKI_BASE = os.getenv("WIKI_BASE", lambda x: WIKI_API.replace("/w/api.php", "/wiki/"))

# @TODO document better this part
WTXT_PAGE_LIMIT = int(os.getenv("WTXT_PAGE_LIMIT", "50"))
WTXT_PAGE_OFFSET = int(os.getenv("WTXT_PAGE_OFFSET", "0"))

CACHE_DRIVER = os.getenv("CACHE_DRIVER", "sqlite")
# @TODO increate default to 23 hours
CACHE_TTL = os.getenv("CACHE_TTL", "3600")  # 1 hour

# @see https://requests-cache.readthedocs.io/en/stable/
requests_cache.install_cache(
    "wikiasbase",
    # /tmp OpenFaaS allow /tmp be writtable even in read-only mode
    # However, is not granted that changes will persist or shared
    db_path="/tmp/wikiasbase_cache.sqlite",
    backend=CACHE_DRIVER,
    expire_after=CACHE_TTL,
    allowable_codes=[200, 400, 404, 500],
)

WIKI_INFOBOXES = os.getenv("WIKI_INFOBOXES", "ValueDescription\nKeyDescription")

# @TODO WIKI_INFOBOXES_IDS
WIKI_INFOBOXES_IDS = os.getenv("WIKI_INFOBOXES_IDS", "{key}={value}\n{key}")
_JSONLD_CONTEXT = (
    # "https://raw.githubusercontent.com/fititnt/osmtags2rive-py/main/context.jsonld"
    "https://wtxt.etica.ai/context.jsonld"
)
_JSONSCHEMA = (
    # "https://raw.githubusercontent.com/fititnt/osmtags2rive-py/main/schema.json"
    "https://wtxt.etica.ai/schema.json"
)


# raise ValueError(WIKI_DATA_LANGS)
# CACHE_DRIVER = os.getenv("CACHE_DRIVER", "sqlite")
# CACHE_TTL = os.getenv("CACHE_TTL", "3600")  # 1 hour

# # @see https://requests-cache.readthedocs.io/en/stable/
# requests_cache.install_cache(
#     "osmapi_cache",
#     # /tmp OpenFaaS allow /tmp be writtable even in read-only mode
#     # However, is not granted that changes will persist or shared
#     db_path="/tmp/osmwiki_cache.sqlite",
#     backend=CACHE_DRIVER,
#     expire_after=CACHE_TTL,
#     allowable_codes=[200, 400, 404, 500],
# )

# @see https://docs.python.org/pt-br/3/library/re.html#re-objects
# @see https://github.com/earwig/mwparserfromhell
# @see https://github.com/siznax/wptools

# @see https://regex101.com/r/rwCoVw/1
# REG = re.compile('<syntaxhighlight lang=\"([a-z0-9]{2,20})\">(.*?)</syntaxhighlight>', flags='gmus')
# REG_SH_GENERIC = re.compile(
#     '<syntaxhighlight lang="(?P<lang>[a-z0-9]{2,20})">(?P<data>.*?)</syntaxhighlight>',
#     flags=re.M | re.S | re.U,
# )

