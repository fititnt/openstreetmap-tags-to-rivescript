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