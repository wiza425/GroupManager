import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from haruka import dispatcher
from haruka.modules.disable import DisableAbleCommandHandler

ART_STRINGS = (
'░░░░▓\
  ░░░▓▓\
 ░░█▓▓█\
 ░██▓▓██\
 ░░██▓▓██\
 ░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░██▓▓██\
 ░░██▓▓██\
 ░██▓▓██\
 ░░██▓▓██\
 ░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░██▓▓██\
 ░░██▓▓██\
 ░██▓▓██\
 ░░██▓▓██\
 ░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░██▓▓██\
 ░░██▓▓██\
 ░██▓▓██\
 ░░██▓▓██\
 ░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░██▓▓██\
 ░░██▓▓██\
 ░██▓▓██\
 ░░██▓▓██\
 ░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░██▓▓██\
 ░░██▓▓██\
 ░██▓▓██\
 ░░██▓▓██\
 ░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░██▓▓██\
 ░░██▓▓██\
 ░██▓▓██\
 ░░██▓▓██\
 ░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░██▓▓██\
 ░░██▓▓██\
 ░██▓▓██\
 ░░██▓▓██\
 ░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░░░██▓▓██\
 ░░░░██▓▓██\
 ░░░██▓▓██\
 ░░██▓▓██\
 ░░██▓▓██\
 ░░██▓▓██\
 ░░██▓▓██\
 ░░██▓▓██\
 ░░██▓▓██\
 ░░░██▓▓███\
 ░░░░██▓▓████\
 ░░░░░██▓▓█████\
 ░░░░░░██▓▓██████\
 ░░░░░░███▓▓███████\
 ░░░░░████▓▓████████\
 ░░░░█████▓▓█████████\
 ░░░█████░░░█████●███\
 ░░████░░░░░░░███████\
 ░░███░░░░░░░░░██████\
 ░░██░@WrEnChz░████\
 ░░░░░░░░░░░░░░░░███\
 ░░░░░░░░░░░░░░░░░░░')

 
@run_async
def art(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(ART_STRINGS))
    else:
      message.reply_text(random.choice(ART_STRINGS))


__help__ = """
- /art : Get some fantastuc Arts.
"""

__mod_name__ = "ART"

ART_HANDLER = DisableAbleCommandHandler("art", art)

dispatcher.add_handler(ART_HANDLER)
