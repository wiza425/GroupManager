import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from haruka import dispatcher
from haruka.modules.disable import DisableAbleCommandHandler

 
MAL_DIALOGUE_STRINGS = (
"`പെമ്പിള്ളേരെ റോട്ടിക്കൂടെ നടക്കാൻ നീ സമ്മതിക്കില്ല , അല്ലേ.......ഡാ, നീയാണീ അലവലാതി ഷാജി അല്ലേ ?`",
    "`വർക്കിച്ചാ യെവൻ പുലിയാണ് കേട്ടാ പുലിയെന്ന് പറഞ്ഞാ വെറും പുലിയല്ല … ഒരു സിംഹം...😜😜 `",
    "`മാമ്മനും അനന്തരവനും കൂടി പണ്ട് ഈഴിര തോർത്തു വെച്ച് പരൽ മീനുകളെ പിടിച്ചു കളിച്ചിട്ടുണ്ടാകും ... പക്ഷെ ആ ഈഴിര വിരിച്ചാൽ സ്രാവിനെ കിട്ടുമെന്നു കരുതരുത് .. ഇത് കാർത്തികേയനാ ...😎😎😎 `",
    "`കഴിഞ്ഞ ഓണത്തിന് കൈപ്പുഴ കുഞ്ഞപ്പന്റെ കയ്യറുത്തപ്പോൾ കട്ടച്ചോരയാ മുഖത്തു തെറിച്ചത് അത്രക്കും വരില്ലല്ലോ ഒരു പീറ ആട്...🤭🤭🤭😜`",
    "`കളി ഹൈറേഞ്ചിലാണെങ്കിലും അങ്ങ് പാരീസിൽ ചെന്ന് ചോദിച്ചാലറിയാം ഈ സാത്താനെ...😎😎😡 `",
    "`എന്റെ ഹൈറേഞ്ചിൽ വന്നിട്ട് എന്റെ പിള്ളേരെ പേടിപ്പിക്കുന്നോടാ നാറികളേ...😡😡😜`",
    "`എവിടെയാടാ നീ അടിച്ചോണ്ട് പോയ എന്റെ നീലക്കുയിൽ 😡😡😜..`",
    "`കൃഷ്ണവിലാസം ഭഗീരഥൻ പിള്ള.. വലിയ വെടി നാല്.. ചെറിയ വെടി നാല്...😜😜🤭`", 
    "`ഇര തേടി വരുന്ന പുലി കെണി തേടി വരില്ല..... പുലിയെ അതിന്റെ മടയിൽ ചെന്ന് വേട്ടയാടി കൊല്ലണം.... അതാണ് കാട്ടിലെ നിയമം...😎😎😇`", 
    "`നീ പോ മോനെ ദിനേശാ...`", "`മരിപ്പിനുള്ള പരിപ്പുവടേം ചായേം ഞാൻ തരുന്നുണ്ട് ഇപ്പോഴല്ല പിന്നെ`", 
    "`സാർ മഹാരാജാസ് കോളേജിൽ പഴേ k.s.u കാരനായിരുന്നല്ലേ അവിടുത്തെ s. F. I പിള്ളേർടെ ഇടി അവസാനത്തേതാണെന്ന് കരുതരുത്...`",
    "`നീയൊക്കെ അര ട്രൗസറും ഇട്ടോണ്ട് അജന്തയിൽ ആദിപാപം കണ്ടോണ്ട് നടക്കണ ടൈമിൽ നമ്മളീ സീൻ വിട്ടതാ നിന്റെയൊക്കെ ഇക്കാനോട് ചോദിച്ചാൽ അറിയാം പോയി ചോദിക്ക് 😎😎😈 `", 
    "`വെല്ലുവിളികൾ ആവാം പക്ഷെ അത് നിന്നെക്കാൾ നാലഞ്ചോണം കൂടുതൽ ഉണ്ടവരോടാവരുത് `", "`ഇവിടെ കിടന്ന് എങ്ങാനും show ഇറക്കാൻ ആണ് പ്ലാൻ എങ്കിൽ പിടിച്ചു തെങ്ങിന്റെ മൂട്ടിലിട്ട് നല്ല വീക്ക് വീക്കും 😡😡😡`", 
    "`ഈ പൂട്ടിന്റെ മുകളിൽ നീ നിന്റെ പൂട്ടിട്ട് പൂട്ടിയാൽ നിന്നെ ഞാൻ പൂട്ടും .. ഒടുക്കത്തെ പൂട്ട് 😡`",
    "`തമ്പുരാൻന്ന് വിളിച്ച അതെ നാവോണ്ട് തന്നെ ചെ** എന്ന് വിളിച്ചതിൽ മനസ്താപണ്ട്..എടോ അപ്പനെന്നു പേരുള്ള തേർഡ് റേറ്റ് ചെ** താനാരാടോ നാട്ടുരാജാവോ 😡😡`", 
    "`ചന്തുവിനെ തോൽപ്പിക്കാൻ ആവില്ല മക്കളേ 😍😍🤗`", 
    "`കൊച്ചി പഴയ കൊച്ചിയെല്ലെന്നറിയാ.... പക്ഷെ ബിലാൽ പഴയ ബിലാൽ തന്നെയാ 😈😈`",
    "`നെട്ടൂരാനോടാണോടാ നിന്റെ കളി 😜😜`", "`ഗോ എവേ സ്റ്റുപ്പിഡ് ഇൻ ദി ഹൗസ് ഓഫ് മൈ വൈഫ്‌ ആൻഡ് ഡോട്ടർ യൂ വിൽ നാട്ട് സീ എനി മിനിറ്റ് ഓഫ് ദി റ്റുഡേ.. എറങ്ങിപ്പോടാ 😜🤭🤣`",
    "`ആണ്ടവൻ ഇത് നിന്റെ കോയമ്പത്തൂരിലെ മായാണ്ടിക്കൊപ്പമല്ല കൊച്ചിയാ വിശ്വനാഥന്റെ കൊച്ചി 😎😎`", 
    "`ഇതെന്റെ പുത്തൻ റെയ്ബാൻ ഗ്ലാസ്സാ ഇത് ചവിട്ടിപൊട്ടിച്ചാ നിന്റെ കാല് ഞാൻ വെട്ടും 😡😡😜`",
    "`നമ്മൾ നമ്മൾ പോലുമറിയാതെ അധോലോകം ആയി മാറിക്കഴിഞ്ഞിരിക്കുന്നു ഷാജിയേട്ടാ...😐 `",
    "`നാലാമത്തെ പെഗ്ഗിൽ ഐസ്ക്യൂബ്സ് വീഴുന്നതിനു മുൻപ് ഞാൻ അവിടെ എത്തും.....😉 `",
    "`പോരുന്നോ എന്റെ കൂടെ!😜 `",
    "`ഡാ ദാസാ... ഏതാ ഈ അലവലാതി.....😒 `",
    "`കാർ എൻജിൻ ഔട്ട് കംപ്ലീറ്റ്ലി.....🥵 `",
    "`അല്ല ഇതാര് വാര്യംപിള്ളിയിലെ മീനാക്ഷി അല്ലയോ... എന്താ മോളെ സ്കൂട്ടറില്....🙈 `",
    "`മോന്തയ്ക്കിട്ട് കൊടുത്തിട്ട് ഒന്ന് എടുത്ത് കാണിച്ചുകൊടുക്ക് അപ്പോൾ കാണും ISI മാർക്ക് 😑 `",
    "`ഇട്ടിട്ട് പോകില്ലെന്ന് ഉറപ്പുള്ള പെണ്ണ്  🤰🤱👩👦 ”`",
    "`ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ....⛪ `",
    "`ഇത് കണ്ണോ അതോ കാന്തമോ...👀 `",
)

MAL_KOZHI_STRINGS = [
    "`വേലക്കാരി ആയിരുന്താലും നീ എൻ മോഹവല്ലി....🥰`", 
    "`ഭവാനി ഒന്നു മനസ്സ് വെച്ചാൽ ഈ കലവറ നമുക്ക് മണിയറ ആക്കാം.....🥰🥰`", 
    "`ഒരു മുത്തം തരാൻ പാടില്ല എന്നൊന്നും അന്റെ ഉപ്പാപ്പ പറഞ്ഞിട്ടുണ്ടാവില്ലല്ല....🥰😜`", 
    "`ശോഭേ ഞാനൊരു വികാര ജീവിയാണ് 😜😜🥰😂 `",
    "`നിനക്കെന്നെ പ്രേമിച്ചൂടെ കൊച്ചേ 😜😜`",
    "`എങ്കിലേ എന്നോട് പറ ഐ ലവ് യൂന്ന് 🥰🥰🥰 `",
    "`പോരുന്നോ എന്റെ കൂടെ 🥰🥰 `",
    "`എനിക്ക് നിന്റെ പുറകിൽ നടക്കാനല്ല, ഒപ്പം നടക്കാനാണ് ഇഷ്ടം 🥰😍`", 
    "`ഓളാ തട്ടമിട്ടു കഴിഞ്ഞാലെന്റെ സാറേ, പിന്നെ ചുറ്റുമുള്ളതൊന്നും കാണാൻ പറ്റൂല്ലാ 😍🥰`",
] 
SHAME_STRINGS = [
   "`തെറി കേട്ടിട്ട് ഇവളുടെ വീട് കൊടുങ്ങല്ലൂർ ഭാഗത്താണെന്ന് തോന്നുന്നു...😜😜`",
   "`പുന്നാര മോളേ😜😜🤭 `", 
   "`ചങ്ക് പറിച്ചു തരുന്ന ചങ്കത്തി കൂടെയുള്ളപ്പോൾ പിന്നെന്തിനാ ലവർ 🥰😜 `",
   "`ഇവൾ നമ്മളേക്കാൾ തറയാടാ...😂😂🤭`",
   "`അഹങ്കാരത്തിന് കയ്യും കാലും വെയ്ക്കാ... എന്നിട്ട് പെണ്ണെന്നു പേരും...🤣🤣😜`",
   "`ആനി മോനെ സ്നേഹിക്കുന്ന പോലെ , മാഗ്ഗിക്ക് എന്നെ സ്നേഹിക്കാമോ...🥰🥰😘`", 
   "`അല്ല ഇതാരാ ! വാര്യംപള്ളിയിലെ മീനാക്ഷിയല്ലയോ ? എന്താ മോളേ സ്കൂട്ടർല്...😜😜🤣`",     
]
VERYSHAME_STRINGS = [
     "`നിന്റെ പേരെന്താന്നാ പറഞ്ഞെ -പൈലി ഡ്രാഗൺപൈലി ഡ്യൂഡ് സാറെന്ന്യല്ലേ പേരിട്ടത്.. എന്തൂള പേരാടാത് അയ്യേ...😛😛😜`", 
     "`ദാമോദരൻ ഉണ്ണി മകൻ ദിൽമൻ ഇടക്കൊച്ചി, പീപ്പിൾ കാൾ മീ ഡ്യൂഡ് 😎😎🤨 `", 
     "`മധ്യതിരുവിതാംകൂർ ഭരിച്ച രാജാവാ പേര് ശശി.. 😛😂🤣 `", 
     "`തീരുമ്പോ തീരുമ്പോ പണി തരാൻ ഞാനെന്താ കുപ്പീന്ന് വന്ന ഭൂതോ... 😇😇🙄`",
     "`ഒന്ന് മിണ്ടാതിരിക്കുവോ.. എന്റെ കോൺസെൻട്രേഷൻ പോണ്.. ദേ ആയുധം വെച്ചുള്ള കളിയാ 😝😝😂`", 
     "`സൂക്ഷിച്ചു നോക്കണ്ടടാ ഉണ്ണീ ഇത് ഞാനല്ല...😇🤣🤣`", 
     "`ഈ യന്ത്രങ്ങളുടെ പ്രവർത്തനമൊന്നും താനെന്നെ പഠിപ്പിക്കേണ്ട ഞാനേ പോളിടെക്‌നിക് പഠിച്ചതാ 😎😎😝 `",
     "`ഡിങ്കോൾഫി അല്ലേ ഇത്രക്ക് ചീപ്പാണോ അര്ടിസ്റ്റ് ബേബി😉😉😜 `",
     "`ആദ്യമായി പ്രേമിച്ച പെണ്ണും ആദ്യമായി അടിച്ച ബ്രാൻഡും ഒരാളും ഒരു കാലത്തും മറക്കില്ല്യ😜😜😎`", 
     "`ഡാ മോനേ അത് ലോക്കാ ഇങ്ങ് പോര്.. ഇങ്ങ് പോര്..😇😇🤭`", 
     "`അടിച്ചതാരാടാ നിന്നെ ആണ്ടവനോ സേഡ്‌ജിയോ അടിച്ചതല്ല ചവിട്ടിയതാ ഷൂസിട്ട കാലുകൊണ്ട് 🤭🤭🤭`",
     "`വസൂ... ദേ തോറ്റു തുന്നം പാടി വന്നിരിക്കുന്നു നിന്റെ മോൻ...🤭🤭😜`", 
     "`വോ ലമ്പേ.... വോ ബാത്തേ.... കോഴീ ന ജാനേ.... ങേ കോഴിയോ 🐓🐓🐓`",
     "`എന്താ? പെൺകുട്ടികൾക്കിങ്ങനെ സിമ്പിൾ ഡ്രെസ് ധരിക്കുന്ന പുരുഷന്മാരെ ഇഷ്ടമല്ലേ ? ഡോണ്ട് ദെ ലൈക് ?😎😜`", 
     "`ലേലു അല്ലു ലേലു അല്ലു ലേലു അല്ലു അഴിച്ചു വിട് 🤣🤣`", 
     "`ഇതെന്താ , എനിക്കുമാത്രം പ്രാന്തായതാണോ അതോ നാട്ടുകാർക്ക് മൊത്തത്തിൽ പ്രാന്തായോ ?😇😇🤣`",
     "`അങ്ങനെ പവനായി ശവമായി.. എന്തൊക്കെ ബഹളമായിരുന്നു.. മലപ്പുറം കത്തി, മെഷീൻഗണ്ണു, ബോംബ്, ഒലക്കേടെ മൂട്...🤭🤣🤣`", 
]

__help__ = """
- /dialogue : Abuse someone in malayalam.
- /Propose : First lines of some random malayalam Songs.
- /shame : Feel Shame of someone
- /veryshame : FEEL VERY VERY SHAME....!
"""

@run_async
def dialogue(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(MAL_DIALOGUE_STRINGS))
    else:
      message.reply_text(random.choice(MAL_DIALOGUE_STRINGS))
      
@run_async
def propose(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(MAL_KOZHI_STRINGS))
    else:
      message.reply_text(random.choice(MAL_KOZHI_STRINGS))
      
@run_async
def shame(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SHAME_STRINGS))
    else:
      message.reply_text(random.choice(SHAME_STRINGS))
      
@run_async
def veryshame(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(VERYSHAME_STRINGS))
    else:
      message.reply_text(random.choice(VERYSHAME_STRINGS))
      
__help__ = """
- /dialogue : Abuse someone with malayalam movie dialogue.
- /Propose : Say some funny malayalam movie proposal dialogues .
- /shame : Say diogues from malayalam movies , use when u feel shame of someone
- /veryshame : FEEL VERY VERY SHAME....!
"""

__mod_name__ = "MAL_DIALOGUES"

DIALOGUE_HANDLER = DisableAbleCommandHandler("dialogue", dialogue)

PROPOSE_HANDLER = DisableAbleCommandHandler("propose", propose)

SHAME_HANDLER = DisableAbleCommandHandler("shame", shame)

VERYSHAME_HANDLER = DisableAbleCommandHandler("veryshame", veryshame)



dispatcher
add_handler(DIALOGUE_HANDLER)
dispatcher.
add_handler(PROPOSE_HANDLER)
dispatcher.
add_handler(SHAME_HANDLER)
dispatcher.
add_handler(VERYSHAME_HANDLER)
