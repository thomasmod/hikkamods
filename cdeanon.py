__version__ = (2, 4, 0)

#            ▀█▀ █ █ █▀█ █▀▄▀█ ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀ █ █▀█ ▄█  
#             https://t.me/netuzb
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta desc: Browse movies by genre and watch them online via bot
# meta pic: https://te.legra.ph/file/fb9f08e6256915a729a12.png
# meta banner: https://te.legra.ph/file/d50815f35c08b9c3dcc90.jpg
# meta developer: @wilsonmods
# scope: hikka_only
# scope: hikka_min 1.3.0

from telethon import events
from .. import loader, utils
from asyncio import sleep

from ..inline.types import InlineCall
from telethon.tl.types import Message
import random

class CDeanonMod(loader.Module):
 """Деанон пользователя
 
> Надеюсь вам понравятся...
> И другие модули: @wilsonmods"""
 
 strings = {
  "name": "CDeanon",
  "bajarilmoqda": "<b>🔥 Деанон пользователя <code>{}</code>...</b>",
  "bajarildi": "<b>🚨 Пользователь <code>{}</code> успешно деанонирован</b>\n   — напоминаю что имя польз. нужно писать без «@»\n\n🎨 <b>Мы тут</b>: <a href='t.me/wilsonmods'>Wilson Hikkamods</a>",
  "info": "🚨 <b>Ну, это не так серьезно, как вы думаете. Тут не будет никаких деанонов, просто введенное вами имя будет прикреплено ко всем существующим ссылкам</b>\n   — Не паникуйте пожалуйста.\n\n🎨 <b>Мы тут</b>: <a href='t.me/wilsonmods'>Wilson Hikkamods</a>",
  "notext": "🚨 <b>Пожалуйста, введите имя пользователя</b>",
  "x": "🔻 Закрыть",
  "ok": "🤡 Понятно",
  "how": "↗️ Как это работает?",
  }
   
 async def deanoncmd(self, message):
  """> [username] без «@» деанон пользователя"""
  
  text = utils.get_args_raw(message) 
  if not text: 
        await message.edit(self.strings("notext", message))
  else:
        deanon = f"{self.strings('bajarildi').format(utils.get_args_raw(message))}"
        await self.inline.form(
                    text = deanon,
                    reply_markup=[
                     [{
                        "text": "👶 Reddit",
                        "url": f"https://www.reddit.com/user/{utils.get_args_raw(message)}"
                     },{
                        "text": "🗳 Telegram",
                        "url": f"https://telegram.me/{utils.get_args_raw(message)}"
                     },{
                        "text": "📺 Youtube",
                        "url": f"https://youtube.com/{utils.get_args_raw(message)}"
                     }],
                     [{
                        "text": "😺 Github",
                        "url": f"https://github.com/{utils.get_args_raw(message)}"
                     },{
                        "text": "🔞 PornHub",
                        "url": f"https://pornhub.com/users/{utils.get_args_raw(message)}"
                     },{
                        "text": "♀️ OnlyFans",
                        "url": f"https://onlyfans.com/{utils.get_args_raw(message)}"
                     }],
                     [{
                        "text": "🐦 Twitter",
                        "url": f"https://www.twitter.com/{utils.get_args_raw(message)}"
                     },{
                        "text": "📸 Instagram",
                        "url": f"https://instagram.com/{utils.get_args_raw(message)}"
                     },{
                        "text": "🧢 VK.com",
                        "url": f"https://vk.com/{utils.get_args_raw(message)}"
                     }],
                     [{
                        "text": "🎨 Blogspot",
                        "url": f"https://{utils.get_args_raw(message)}.blogspot.com"
                     },{
                        "text": "🐚 Gitlab",
                        "url": f"https://gitlab.com/{utils.get_args_raw(message)}"
                     },{
                        "text": "🎧 SoundCloud",
                        "url": f"https://soundcloud.com/{utils.get_args_raw(message)}"
                     }],                                
                     [{
                        "text": "🌇 Pinterest",
                        "url": f"https://www.pinterest.com/{utils.get_args_raw(message)}"
                     },{
                        "text": "👥 OK.ru",
                        "url": f"https://ok.ru/{utils.get_args_raw(message)}"
                     },{
                        "text": "💻 Steam",
                        "url": f"https://steamcommunity.com/id/{utils.get_args_raw(message)}"
                     }],
                     [{
                        "text": "⭐ Dumpor",
                        "url": f"https://dumpor.com/v/{utils.get_args_raw(message)}"
                     },{
                        "text": "🤖 Roblox",
                        "url": f"https://www.roblox.com/user.aspx?username={utils.get_args_raw(message)}"
                     },{
                        "text": "🍀 Nitter",
                        "url": f"https://nitter.net/{utils.get_args_raw(message)}"
                     }],
                     [{
                        "text": "🎙️ Smule",
                        "url": f"https://www.smule.com/{utils.get_args_raw(message)}"
                     },{
                        "text": "📝 TamTam",
                        "url": f"https://tamtam.chat/{utils.get_args_raw(message)}"
                     },{
                        "text": "🎮 Twitch",
                        "url": f"https://www.twitch.tv/{utils.get_args_raw(message)}"
                     }],
                     [{
                        "text": "🍙 TikTok",
                        "url": f"https://vm.tiktok.com/{utils.get_args_raw(message)}"
                     },{
                        "text": "🍑 Likee",
                        "url": f"https://likee.video/@{utils.get_args_raw(message)}"
                     },{
                        "text": "🖼️ Freepik",
                        "url": f"https://www.freepik.com/{utils.get_args_raw(message)}"
                     }],
                     [{
                            "text": self.strings("how"),
                            "callback": self.how
                     }],
                     [{
                            "text": self.strings("x"), 
                            "action": "close"
                     }],
                     ],      **{"photo": "https://te.legra.ph/file/d50815f35c08b9c3dcc90.jpg"},
                    message=message,
                    )                                           
             
 async def how(self, call: InlineCall) -> None:                     
                     await call.edit(                                       
                     text = f"{self.strings('info')}",
                     reply_markup=[
                     [{
                        "text": "🎨 Больше модули",
                        "url": "t.me/wilsonmods"
                     }],
                     [{
                            "text": self.strings("ok"), 
                            "action": "close"
                     }]],   
                            **{"photo": "https://te.legra.ph/file/d50815f35c08b9c3dcc90.jpg"},
                )              
                                  