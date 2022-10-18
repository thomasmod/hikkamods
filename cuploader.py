__version__ = (3, 4, 0)
          
#            ▀█▀ █ █ █▀█ █▀▄▀█ ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀ █ █▀█ ▄█  
#           https://t.me/netuzb
#
#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://te.legra.ph/file/12605828ab1dc52569739.png
# meta banner: https://te.legra.ph/file/407a0817f59ec861d031b.jpg
# meta developer: @wilsonmods | @hikarimods
# scope: hikka_only
# scope: hikka_min 1.2.10

import imghdr
import io
import random
import re
import os

import requests
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import Message
from .. import loader, utils


@loader.tds
class UploadToProviderMod(loader.Module):
    """Хостинг-провайдеры «skynet», «imgur», «oxo»"""    

    strings = {
        "name": "📤 CUploader",        
        "noargs": "🚫 <b>File not specified</b>",
        "err": "🚫 <b>loading error</b>", 
        "uploaded": '🌄 <b>File uploaded successfully.</b>\n',
        "imgur_blocked": "🚫 <b>Unblock @ImgUploadBot</b>",
        "not_an_image": "🚫 <b>This platform only supports images</b>",
        "to_module": "🔥 <b>Direct link for the install module:</b>",
        "_cmd_doc_imgur": "Upload to imgur.com",
        "_cmd_doc_oxo": "Upload to 0x0.st",
        "_cmd_doc_x0": "Upload to x0.at",
        "_cmd_doc_skynet": "Upload to SkyNet decentralized platform",
        "_cls_doc": "Upload files to different hosting",
        "uploading": "🚀 <b>Loading...</b>",
        "yopish": "🔻 Close",
    }
    
    strings_ru = {      
        "noargs": "🚫 <b>Файл не указан</b>",
        "err": "🚫 <b>Ошибка загрузки</b>", 
        "uploaded": '🌄 <b>Файл успешно загружен.</b>\n',
        "imgur_blocked": "🚫 <b>Разблокируй @ImgUploadBot</b>",
        "not_an_image": "🚫 <b>Эта платформа поддерживает только изображения</b>",
        "to_module": "🔥 <b>Прямая ссылка для установки модуля:</b>",
        "_cmd_doc_imgur": "Загрузить на imgur.com",
        "_cmd_doc_oxo": "Загрузить на 0x0.st",
        "_cmd_doc_x0": "Загрузить на x0.at",
        "_cmd_doc_skynet": "Загрузить на децентрализованную платформу SkyNet",
        "_cls_doc": "Загружает файлы на различные хостинги",
        "uploading": "🚀 <b>Загрузка...</b>",
        "yopish": "🔻 Закрыть",        
    }
    
    strings_uz = {      
        "noargs": "🚫 <b>Fayl ko'rsatilmadi</b>",
        "err": "🚫 <b>yuklashda xatolik</b>", 
        "uploaded": '🌄 <b>Fayl muvaffaqiyatli yuklandi.</b>\n',
        "imgur_blocked": "🚫 <b>@ImgUploadBot qora ro'yhatdan chiqaring!</b>",
        "not_an_image": "🚫 <b>Bu platforma faqat rasmlarni yuklaydi!</b>",
        "to_module": "🔥 <b>Modul o'rnatish uchun to'g'ridan-to'g'ri havola:</b>",
        "_cmd_doc_imgur": "imgur.com hostiga yuklash",
        "_cmd_doc_oxo": "0x0.st hostiga yuklash",
        "_cmd_doc_x0": "x0.at hostiga yuklash",
        "_cmd_doc_skynet": "Maxsuslashtirilgan SkyNet hostingiga yuklash",
        "_cls_doc": "Duch kelgan hostinga yuklash",
        "uploading": "🚀 <b>Yuklanmoqda...</b>",
        "yopish": "🔻 Yopish",        
    }
	
    async def get_media(self, message: Message):
        reply = await message.get_reply_message()
        m = None
        if reply and reply.media:
            m = reply
        elif message.media:
            m = message
        elif not reply:
            await utils.answer(message, self.strings("noargs"))
            return False

        if not m:
            file = io.BytesIO(bytes(reply.raw_text, "utf-8"))
            file.name = "file.txt"
        else:
            file = io.BytesIO(await self._client.download_media(m, bytes))
            file.name = (
                m.file.name
                or (
                    "".join(
                        [
                            random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
                            for _ in range(16)
                        ]
                    )
                )
                + m.file.ext
            )

        return file

    async def get_image(self, message: Message):
        file = await self.get_media(message)
        if not file:
            return False

        if imghdr.what(file) not in ["gif", "png", "jpg", "jpeg", "tiff", "bmp"]:
            await utils.answer(message, self.strings("not_an_image"))
            return False

        return file

    async def skycmd(self, message: Message):
        """> Загрузить в хостинг «SkyNet»"""
        message = await utils.answer(message, self.strings("uploading"))
        file = await self.get_media(message)
        if not file:
            return

        try:
            skynet = await utils.run_sync(
                requests.post,
                "https://siasky.net/skynet/skyfile",
                files={"file": file},
            )
        except ConnectionError:
            await utils.answer(message, self.strings("err"))
            return
        
        sky = f"<code>https://siasky.net/{skynet.json()['skylink']}</code>\n\n{self.strings('to_module')}\n<code>.dlmod https://siasky.net/{skynet.json()['skylink']}</code>"
        await self.inline.form(
                    self.strings("uploaded", message) + sky,
                    reply_markup=[
                    	[{
							"text": "🌐 Посмотреть", 
							"url": f"https://siasky.net/{skynet.json()['skylink']}"
						},
						{
							"text": "↗️ Поделиться", 
							"url": f"https://t.me/share/url?url=https://siasky.net/{skynet.json()['skylink']}"
						}],						
				        [{"text": self.strings("yopish"), "action": "close"}],
                    ],
                    ttl=10,
                    message=message,
                )

    async def imgurcmd(self, message: Message):
        """> Загрузить в провайдер «imgur»"""
        message = await utils.answer(message, self.strings("uploading"))
        file = await self.get_image(message)
        if not file:
            return

        chat = "@ImgUploadBot"

        async with self._client.conversation(chat) as conv:
            try:
                m = await conv.send_message(file=file)
                response = await conv.get_response()
            except YouBlockedUserError:
                await utils.answer(message, self.strings("imgur_blocked"))
                return

            await m.delete()
            await response.delete()

            try:
                url = (
                    re.search(
                        r'<meta property="og:image" data-react-helmet="true"'
                        r' content="(.*?)"',
                        (await utils.run_sync(requests.get, response.raw_text)).text,
                    )
                    .group(1)
                    .split("?")[0]
                )
            except Exception:
                url = response.raw_text
            aa = f"<code>{url}</code>"
            await self.inline.form(
                    self.strings("uploaded", message) + aa,
                    reply_markup=[
                     [{
							"text": "🌐 Посмотреть", 
							"url": f"{url}"
					 },
					 {
							"text": "↗️ Поделиться", 
							"url": f"https://t.me/share/url?url={url}"
					 }],
                     [{"text": self.strings("yopish"), "action": "close"}],
                     ], **{"photo": f"{url}"},
                    ttl=10,
                    message=message,
                )

    async def oxocmd(self, message: Message):
        """> Загрузить в хостинг «oxo»"""
        message = await utils.answer(message, self.strings("uploading"))
        file = await self.get_media(message)
        if not file:
            return

        try:
            oxo = await utils.run_sync(
                requests.post,
                "https://0x0.st",
                files={"file": file},
            )
        except ConnectionError:
            await utils.answer(message, self.strings("err"))
            return

        url = oxo.text        
        aa = f"<code>{url}</code>"
        await self.inline.form(
                    self.strings("uploaded", message) + aa,
                    reply_markup=[
                     [{
							"text": "🌐 Посмотреть", 
							"url": f"{url}"
					 },
					 {
							"text": "↗️ Поделиться", 
							"url": f"https://t.me/share/url?url={url}"
					 }],
                     [{"text": self.strings("yopish"), "action": "close"}],
                     ],
                    ttl=10,
                    message=message,
                )
