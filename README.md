# openstreetmap-tags-to-rivescript
**Convert of openstreetmap/id-tagging-schema to RiveScript, the Artificial Intelligence Scripting Language (alternative to AIML)**

## Quickstart

### Install

No pip release yet, install from GitHub

```bash
pip install git+https://github.com/fititnt/openstreetmap-tags-to-rivescriptt@main
```

### Fetch cache

```bash
# Prepare the cache directory
git clone https://github.com/openstreetmap/id-tagging-schema.git ./id-tagging-schema

osmtags2rive --language=pt > brain/osm-tagging-pt.rive
```

### Test

#### Python example
Using Rive Python interpreter (there are other for other programming languages)
from https://github.com/aichaos/rivescript-python

```bash
# install the script
pip install rivescript

python shell.py
```

```python
# file shell.py

from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

while True:
    msg = input('You> ')
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print ('Bot>', reply)
```


# Disclaimers
<!--
TODO see https://wiki.osmfoundation.org/wiki/Trademark_Policy
-->

OpenStreetMap™ is a trademark of the OpenStreetMap Foundation, and is used with their permission.
This project is not endorsed by or affiliated with the OpenStreetMap Foundation. (via [OSMF Trademark_Policy](https://wiki.osmfoundation.org/wiki/Trademark_Policy))

# License


[![Public Domain](https://i.creativecommons.org/p/zero/1.0/88x31.png)](LICENSE)

Public domain