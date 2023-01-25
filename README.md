# openstreetmap-tags-to-rivescript
**Convert of openstreetmap/id-tagging-schema to [RiveScript](https://www.rivescript.com/about), the Artificial Intelligence Scripting Language (alternative to AIML)**

[![Pypi: osmtags2rive](https://img.shields.io/badge/python%20pypi-osmtags2rive-brightgreen[Python] "Pypi: osmtags2rive")](https://pypi.org/project/osmtags2rive)
[![GitHub](https://img.shields.io/badge/GitHub-fititnt%2Fopenstreetmap--tags--to--rivescript-lightgrey?logo=github&style=social[fititnt/openstreetmap-tags-to-rivescript] "GitHub")](https://github.com/fititnt/openstreetmap-tags-to-rivescript)

## Quickstart

### Install

<s>No pip release yet, install from GitHub:</s> <s><code>pip install https://github.com/fititnt/openstreetmap-tags-to-rivescript/archive/main.zip</code></s>

Just install via pypi:

```bash
pip install --upgrade osmtags2rive

# To see all options
osmtags2rive --help
```

### Fetch cache

A copy of <https://github.com/openstreetmap/id-tagging-schema> on local disk is necessary.
The following example saves on a path that is discovered by the cli tool.

```bash
# Prepare the cache directory
git clone https://github.com/openstreetmap/id-tagging-schema.git ./id-tagging-schema
```

The exact path can be customized with `--path-id-tagging-schema` option.

### Generate RiveScript

```bash
osmtags2rive --language=pt > example/brain/osm-tagging_pt.rive
osmtags2rive --language=pt --reverse-index > example/brain/osm-tagging-reverse_pt.rive
```

<!--
To regenerate again example

osmtags2rive --language=pt > example/brain/osm-tagging_pt.rive
osmtags2rive --language=pt --reverse-index > example/brain/osm-tagging-reverse_pt.rive
-->

## Extras

### Quickstart on how to use the generated RiveScripts

Check [Rivescript website page for interpreters](https://www.rivescript.com/interpreters) for other programming languages than python or the online playground.
They all have a similar interface:
allow you to deposit all files in a directory which is loaded by your interpreter.

#### Online playground
- https://play.rivescript.com/ <sup>recommended</sup>
- https://www.rivescript.com/try

Copy and paste the contents of all the files and run it.

#### Python example
Using Rive Python interpreter from https://github.com/aichaos/rivescript-python

```bash
# install the rivescript python library
pip install rivescript

# Run your application.
# This one is a very simple (no integration with Telegram, Slack, etc) as proof of concept.
python shell.py
```

```python
# file shell.py

from rivescript import RiveScript

# bot = RiveScript(utf8=True)
bot = RiveScript()
bot.load_directory("./example/brain")
bot.sort_replies()

while True:
    msg = input('You> ')
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print ('Bot>', reply)
```

**Example of interaction** (may change)
```bash
You> highway=residential 
Bot> OpenStreetMap preset highway/residential def. Rua residencial
You> estrada desconhecida
Bot> [ERR: No Reply Matched]
You> /quit
```

> @TODO fix spaces on reverse index; "estrada desconhecida", not only strictly "estradadesconhecida"


# Disclaimers
<!--
TODO see https://wiki.osmfoundation.org/wiki/Trademark_Policy
-->

OpenStreetMap™ is a trademark of the OpenStreetMap Foundation, and is used with their permission.
This project is not endorsed by or affiliated with the OpenStreetMap Foundation. (via [OSMF Trademark_Policy](https://wiki.osmfoundation.org/wiki/Trademark_Policy))

# License


[![Public Domain](https://i.creativecommons.org/p/zero/1.0/88x31.png)](LICENSE)

Public domain