mport random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from haruka import dispatcher
from haruka.modules.disable import DisableAbleCommandHandler


ART_STRINGS = (
   "( ͡° ͜ʖ ͡°)",
  
    "¯\_(ツ)_/¯",

   "▄︻̷̿┻̿═━一",

   "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
  
    "ʕ•ᴥ•ʔ"
   )


@run_async
def art(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(FACES_STRINGS))
    else:
      message.reply_text(random.choice(FACES_STRINGS))




__help__ = """
- /faces : React to someones message with some faces.
"""

__mod_name__ = "FACES"

FACES_HANDLER = DisableAbleCommandHandler("faces", faces)

dispatcher.add_handler(FACES_HANDLER)
