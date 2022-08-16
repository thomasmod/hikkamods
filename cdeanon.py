__version__ = (2, 1, 4)

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

import random

class CDeanonMod(loader.Module):
 """Деанон пользователя
 
> Надеюсь вам понравятся...
> И другие модули: @wilsonmods"""
 
 strings = {
  "name": "CDeanon",
  "bajarilmoqda": "<b>🔥 Деанон пользователя <code>{}</code>...</b>",
  "bajarildi": "<b>🚨 Пользователь <code>{}</code> успешно деанонирован</b>\n   — напоминаю что имя польз. нужно писать без «@»",
  }
   
 async def deanoncmd(self, message):
  """> [username] без «@» деанон пользователя"""
  
  text = utils.get_args_raw(message)
  await message.edit(f"{self.strings('bajarilmoqda').format(text)}")
  await sleep(2, 0)
  await message.delete()
  deanon = f"{self.strings('bajarildi').format(text)}"
  await self.inline.form(
                    text = deanon,
                    reply_markup=[
                     [{
                        "text": "👶 Reddit",
                        "url": f"https://www.reddit.com/user/{text}"
                     },{
                        "text": "🗳 Telegram",
                        "url": f"https://telegram.me/{text}"
                     },{
                        "text": "📺 Youtube",
                        "url": f"https://youtube.com/{text}"
                     }],
                     [{
                        "text": "😺 Github",
                        "url": f"https://github.com/{text}"
                     },{
                        "text": "🔞 PornHub",
                        "url": f"https://pornhub.com/users/{text}"
                     },{
                        "text": "♀️ OnlyFans",
                        "url": f"https://onlyfans.com/{text}"
                     }],
                     [{
                        "text": "🐦 Twitter",
                        "url": f"https://www.twitter.com/{text}"
                     },{
                        "text": "📸 Instagram",
                        "url": f"https://instagram.com/{text}"
                     },{
                        "text": "🧢 VK.com",
                        "url": f"https://vk.com/{text}"
                     }],
                     [{
                        "text": "🎨 Blogspot",
                        "url": f"https://{text}.blogspot.com"
                     },{
                        "text": "🐚 Gitlab",
                        "url": f"https://gitlab.com/{text}"
                     },{
                        "text": "🎧 SoundCloud",
                        "url": f"https://soundcloud.com/{text}"
                     }],
                     [{
                        "text": "🌇 Pinterest",
                        "url": f"https://www.pinterest.com/{text}"
                     },{
                        "text": "👥 OK.ru",
                        "url": f"https://ok.ru/{text}"
                     },{
                        "text": "💻 Steam",
                        "url": f"https://steamcommunity.com/id/{text}"
                     }],
                     [{
                        "text": "⭐ Dumpor",
                        "url": f"https://dumpor.com/v/{text}"
                     },{
                        "text": "🤖 Roblox",
                        "url": f"https://www.roblox.com/user.aspx?username={text}"
                     },{
                        "text": "🍀 Nitter",
                        "url": f"https://nitter.net/{text}"
                     }],
                     [{
                        "text": "🎙️ Smule",
                        "url": f"https://www.smule.com/{text}"
                     },{
                        "text": "📝 TamTam",
                        "url": f"https://tamtam.chat/{text}"
                     },{
                        "text": "🎮 Twitch",
                        "url": f"https://www.twitch.tv/{text}"
                     }],
                     [{
                        "text": "🍙 TikTok",
                        "url": f"https://vm.tiktok.com/{text}"
                     },{
                        "text": "🍑 Likee",
                        "url": f"https://likee.video/@{text}"
                     },{
                        "text": "🖼️ Freepik",
                        "url": f"https://www.freepik.com/{text}"
                     }],
                     ],  **{"photo": "https://te.legra.ph/file/d50815f35c08b9c3dcc90.jpg"},
                    message=message,
                    )
