__version__ = (1, 1, 1)
          
#            ▀█▀  █ █ █▀█  █▀▄▀█  ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀  █ █▀█ ▄█  
#            https://t.me/netuzb
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://te.legra.ph/file/c0292154a0e8bbe2ba654.png
# meta banner: https://te.legra.ph/file/71b59ef7904a7742c8109.jpg
# meta developer: @wilsonmods
# scope: hikka_only
# scope: hikka_min 1.3.2

from .. import loader, utils
import asyncio
import requests
from telethon.tl.types import DocumentAttributeFilename

wilson_warn = "🚨 "
wilson_rocket = "🚀 "
wilson_link = "✅ "
wilson_view = "↗️ "
wilson_share = "💌 "
wilson_media = "🎨 "


class ActuallTelegraphMod(loader.Module):
	"""Uploading a photo/gif/picture to actuall telegraph"""
	
	strings = {
               "name": "📌 Actuall-Telegraph",
               "wilson_no_reply": wilson_warn + "<b>Reply to media file</b>",
               "wilson_done": wilson_media + "<b>The address where the media file is saved</b> |",
               "wilson_succes": wilson_link + "<b>Link ready</b>\n",
               "wilson_wait": wilson_rocket + "<b>Uploading...</b>",
               "wilson_close": wilson_warn + "Close",
               "wilson_view": wilson_view + "View",
               "wilson_share": wilson_share + "Share",
               }
               

	strings_ru = {
               "wilson_no_reply": wilson_warn + "<b>В ответ медияфайл...</b>",
               "wilson_done": wilson_media + "<b>️Ссылка на медиафайл</b>:",
               "wilson_succes": wilson_link + "<b>Ссылка готова</b>\n",
               "wilson_wait": wilson_rocket + "<b>Загрузка...</b>",
               "wilson_close": wilson_warn + "Закрыть",
               "wilson_view": wilson_view + "Посмотреть",
               "wilson_share": wilson_share + "Share",
               }
	
	strings_uz = {
               "wilson_no_reply": wilson_warn + "<b>Kerakli faylga javob tariqasida</b>",
               "wilson_done": wilson_media + "<b>Quyidagi manzilga sizning faylingiz joylandi</b> |",
               "wilson_succes": wilson_link + "<b>Havola tayyor</b>\n",
               "wilson_wait": wilson_rocket + "<b>Yuklanmoqda...</b>",
               "wilson_close": wilson_warn + "Yopish",
               "wilson_view": wilson_view + "ko'rish",
               "wilson_share": wilson_share + "Ulashish",
               }

	def __init__(self):
	    self.config = loader.ModuleConfig(
	        loader.ConfigValue(
                "wilson_share",
                f"{wilson_share}Share",
                doc=lambda: self.strings("wilson_share"),
            ),            
            loader.ConfigValue(
                "wilson_view",
                f"{wilson_view}View",
                doc=lambda: self.strings("wilson_view"),
            ),
        )
	
	async def cphcmd(self, message):
             """> Set up buttons for the module"""
             name = self.strings("name")
             await self.allmodules.commands["config"](
             await utils.answer(message, f"{self.get_prefix()}config {name}")
             )
	
	async def phcmd(self, message):
			"""> Uploading a photo/gif/picture to Telegra.ph"""
			await message.edit(f"{self.strings('wilson_wait')}")
			if message.is_reply:
				reply_message = await message.get_reply_message()
				data = await check_media(reply_message)
				if isinstance(data, bool):
					await message.edit(f"{self.strings('wilson_no_reply')}")
					return
			else:
				await message.edit(self.strings("wilson_no_reply", message))
				return
					
				
			file = await message.client.download_media(data, bytes)
			path = requests.post('https://te.legra.ph/upload', files={'file': ('file', file, None)}).json()
			try:
				thom_link = 'https://te.legra.ph'+path[0]['src']
			except KeyError:
				thom_link = path["error"]			
			await self.inline.form(
                    text = f"{self.strings('wilson_succes')}{self.strings('wilson_done')} <code>{thom_link}</code>",
                    reply_markup=[
                    [{
                        "text": self.config['wilson_share'],
                        "url": f"https://t.me/share/url?url=Check it: {thom_link}"
                     }],
                     [{
                        "text": self.config['wilson_view'],
                        "url": f"{thom_link}"
                     },{
                        "text": f"{self.strings('wilson_close')}", "action": "close"
                     }]], 
                        **{"photo": f"{thom_link}"},
                        message=message,
                     )

async def check_media(reply_message):
	if reply_message and reply_message.media:
		if reply_message.photo:
			data = reply_message.photo
		elif reply_message.document:
			if DocumentAttributeFilename(file_name='stick.tgs') in reply_message.media.document.attributes:
				return False
			if reply_message.audio or reply_message.voice:
				return False
			data = reply_message.media.document
		else:
			return False
	else:
		return False
	if not data or data is None:
		return False
	else:
		return data 
