__version__ = (1, 0, 1)

#            ▀█▀ █ █ █▀█ █▀▄▀█ ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀ █ █▀█ ▄█  
#             https://t.me/netuzb
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta desc: True or False
# meta pic: https://te.legra.ph/file/302a4cff5a0d14fb3cfd0.png
# meta banner: https://te.legra.ph/file/1a095e49fb817f622c722.jpg
# meta developer: @wilsonmods
# scope: hikka_only
# scope: hikka_min 1.3.0

import logging
import random

from telethon.tl.types import Message
from .. import loader, utils
logger = logging.getLogger(__name__)

# EMOJI PLACE 
emoji_dzin = "✨ "
emoji_done = "💬 "
emoji_true = "✅ "
emoji_false = "🚫 "

@loader.tds
class TrueOrFalseMod(loader.Module):
    """The module will tell you if it's true or false"""

    strings = {
        "name": "🎲 True-or-False",       
        "yes": emoji_true + "True",
        "no": emoji_false + "False",
        "_cfg_hm_text": "Change result text",
    }

    strings_ru = {        
        "yes": emoji_true + "Правда",
        "no": emoji_false + "Ложь",
        "_cfg_hm_text": "Изменить текст результата",
    }
    
    strings_uz = {        
        "yes": emoji_true + "Rost",
        "no": emoji_false + "Yolg'on",
        "_cfg_hm_text": "Natija bandi yozuvini o'zgartirish",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(                        
            loader.ConfigValue(
                "hm_text",
                "Here is your result 👇",
                lambda: self.strings("_cfg_hm_text"),
            ),            
        )

    @loader.command(
        ru_doc=(
            "Показывает правду или ложь"
        )
    )
    async def tof(self, message: Message):
        """[text] - True or False"""
        args = utils.get_args_raw(message)
        tfas = [f"{self.strings('yes')}", f"{self.strings('no')}"]
        tf = f"{random.choice(tfas)}"        
        await self.inline.form(
            text = f"{emoji_dzin}" + self.config["hm_text"] + f"\n\n{emoji_done}<b>Text</b>: <code>{args}</code>",
            message=message, 
            reply_markup=[
            [{
                "text": f"{tf}", 
                "action": "close"                
            }],
        ],                 
    )   
