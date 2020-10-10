# For @UniBorg

# Courtesy @yasirsiddiqui

"""

.bye

"""

import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

import haruka.modules.fun_strings as fun_strings
from haruka import dispatcher
from haruka.modules.disable import DisableAbleCommandHandler
from haruka.modules.helper_funcs.chat_status import is_user_admin
from haruka.modules.helper_funcs.extraction import extract_user

@borg.on(admin_cmd(pattern="bye", outgoing=True))

async def leave(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("`People here are so dumb 😑. I'm leaving.`")

        time.sleep(3)

        if '-' in str(e.chat_id):

            await borg(LeaveChannelRequest(e.chat_id))

        else:

            await e.edit('`This is Not A Chat. Please use this in groups :/`')