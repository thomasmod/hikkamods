__version__ = (2, 1, 4)

#            ▀█▀ █ █ █▀█ █▀▄▀█ ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀ █ █▀█ ▄█  
#             https://t.me/netuzb
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta desc: This is the module in which my pictures are collected
# meta pic: https://te.legra.ph/file/c2a2e80babba6113cbf60.png
# meta banner: https://te.legra.ph/file/5e285dfcd5521028e4edf.jpg
# meta developer: @wilsonmods
# scope: hikka_only
# scope: hikka_min 1.3.1

import asyncio
import functools
import requests
from .. import loader, utils

from telethon.tl.types import Message
from ..inline.types import InlineCall

# EMOJIES ROOM
emoji_write = "📝 "
emoji_photo = "✨ "
emoji_close = "🔻 "
emoji_book = "📚 "
emoji_remove = "🚫 "
emoji_back = "↩️ "

@loader.tds
class MyGalleryMod(loader.Module):
    """> This is the module in which my pictures are collected"""

    strings = {
            "name": "🖼️ MyGallery",
            "_add_photo": emoji_photo + "Provide a link to add an image",
            "_main_text": emoji_write + "The main text can be spoken here",
            "tt_text": "<b>Select the required Tutorial type</b> 👇",
            "tt_close": emoji_close + "Close",
            "tt_back": emoji_back + "Back",
            "btn_how_add": emoji_book + "How to add text?",
            "btn_how_remove": emoji_remove + "How to remove photo?",
            "txt_how_add": "<b>To add a photo to the gallery you need to repeat these tasks:</b>\n\n<i>1. Open <code>.glcf</code>\n2. Tap on «ADD_PHOTO_LINK»\n3. And tap on «➕ Add item»\n3. Enter photo link</i>",
            "txt_how_remove": "<b>To add a photo to the gallery you need to repeat these tasks:</b>\n\n<i>1. Open <code>.glcf</code>\n2. Tap on «ADD_PHOTO_LINK»\n3. And tap on «➖ Remove item»\n4. Submit an available photo link</i>",
            }
    
    strings_ru = {
             "_add_photo": emoji_photo + "Укажите ссылку для добавления изображения",
             "_main_text": emoji_write + "Здесь можно произнести основной текст",
             "tt_text": "<b>Выберите нужный тип обучения</b> 👇",
             "tt_close": emoji_close + "Закрыть",
             "tt_back": emoji_back + "Назад",
             "btn_how_add": emoji_book + "Как добавить текст?",
             "btn_how_remove": emoji_remove + "Как удалить фото?",
             "txt_how_add": "<b>Чтобы добавить фотографию в галерею, вам нужно повторить следующие действия:</b>\n\n<i>1. Откройте <code>.glcf</code>\n2. Нажмите на  «ADD_PHOTO_LINK»\n3. Нажмите «➕ Добавить элемент»\n3. Введите ссылку на фото</i>",
             "txt_how_remove": "<b>Чтобы добавить фото в галерею, вам нужно повторить следующие действия:</b>\n\n<i>1. Откройте <code>.glcf</code>\n2. Нажмите на  «ADD_PHOTO_LINK»\n3. Нажмите «➖ Удалить элемент»\n4. Отправьте доступную ссылку на фото</i>",
             }

    async def client_ready(self, client, db):
        self._client = client
    
    def __init__(self):
        self.config = loader.ModuleConfig(         
            loader.ConfigValue(
                "ADD_PHOTO_LINK",                
                [
                "https://te.legra.ph/file/15d3fab9da288e4d7ebb7.jpg",
                "https://te.legra.ph/file/f05b72c384539dd6a6816.jpg",
                "https://te.legra.ph/file/f5066daf455931bb735f1.jpg",
                ],
                lambda: self.strings("_add_photo"),
                validator=loader.validators.Series(validator=loader.validators.Link()),
                ),
                loader.ConfigValue(
                "MAIN_TEXT",
                "<i>Add your first text here</i>",
                doc=lambda: self.strings('_main_text'),
            ),                      
        )
        
    @loader.command(
        ru_doc=(" > Открыть мою галерею"))
    async def gl(self, message: Message):
        """ > Open my gallery"""
        photo = self.config['ADD_PHOTO_LINK']
        await self.inline.gallery(
            caption=lambda: self.config['MAIN_TEXT'],
            message=message,
            next_handler = photo,
            preload=5,
        )
    
    @loader.command(
        ru_doc=(" > Открыть конфигурацию галереи"))
    async def glcf(self, message):       
        """ > Open gallery configuration"""
        name = self.strings("name")
        await self.allmodules.commands["config"](
        await utils.answer(message, 
        f"{self.get_prefix()}config {name}")
        )
    
    @loader.command(        
        ru_doc=(" > Тутор как добавить фото в MyGallery"))
    async def gltutor(self, message):       
        """ > Tutor how to add a photo to the MyGallery"""
        await self.inline.form(
               self.strings('tt_text'),
               message=message,
               reply_markup=[
               [{
                    "text": f"{self.strings('btn_how_add')}",
                    "callback": self._how_add
               }],
               [{
                    "text": f"{self.strings('btn_how_remove')}",
                    "callback": self._how_remove
               }]],                  
                    **{"gif": "https://t.me/anonyusa/138"},
         )
    
    async def _main(self, call: InlineCall):       
        await call.edit(
               self.strings('tt_text'),
               reply_markup=[
               [{
                    "text": f"{self.strings('btn_how_add')}",
                    "callback": self._how_add
               }],
               [{
                    "text": f"{self.strings('btn_how_remove')}",
                    "callback": self._how_remove
               }]],
                    **{"gif": "https://t.me/anonyusa/138"},                  
         )
    
    async def _how_add(self, call: InlineCall):
        await call.edit(
            self.strings("txt_how_add"),
            reply_markup=[           
            [{
                 "text": self.strings("tt_back"), 
                 "callback": self._main
            },{
                 "text": self.strings("tt_close"), 
                 "action": "close"
            }]],   
                 **{"gif": "https://t.me/anonyusa/136"},              
       )
    
    async def _how_remove(self, call: InlineCall):
        await call.edit(
            self.strings("txt_how_remove"),
            reply_markup=[           
            [{
                 "text": self.strings("tt_back"), 
                 "callback": self._main
            },{
                 "text": self.strings("tt_close"), 
                 "action": "close"
            }]],  
                 **{"gif": "https://t.me/anonyusa/137"},               
       )
            
