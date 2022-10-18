__version__ = (1, 0, 0)

#            ▀█▀ █ █ █▀█ █▀▄▀█ ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀ █ █▀█ ▄█  
#             https://t.me/netuzb
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta desc: Generator of random cringe photos
# meta pic: https://te.legra.ph/file/546396354d6a3161e71bb.png
# meta banner: https://te.legra.ph/file/f61d5478f5aeead963421.jpg
# meta developer: @wilsonmods

# scope: hikka_only
# scope: hikka_min 1.3.0

from .. import loader, utils
import random 

@loader.tds
class RandomCringeMod(loader.Module):
    """Random cringe generate"""
    
    strings = {
        "name": "🍁 RandomCringe",
        "done": "<b>✅ Done!</b>",
        "add_photo_tutorial": (
            "Here you will be able to add unlimited"
            " Cringe photos.  Click the «➕ Add item»"
            " button and enter the link for the photo"
            " (format .jpg, .png, .webp, etc.)"
            ),
        }
        
    strings_ru = {
        "done": "<b>✅ Готов!</b>",
        "add_photo_tutorial": (
            "Здесь вы сможете добавлять неограниченное"
            " количество фотографий Кринжа. Нажмите кнопку"
            " «➕ Добавить элемент» и введите ссылку на фото"
            " (формат .jpg, .png, .webp и т.д.)"
            ),
        }
    
    strings_uz = {
        "done": "<b>✅ Tayyor!</b>",
        "add_photo_tutorial": (
            "Bu yerda siz cheksizlik miqdorda"
            " Cringe surtlarini joylay olasiz. Joylash uchun"
            " «➕ Elenent q'shish» orqali rasmga havola ko'rsating"
            " (formatlar .jpg, .png, .webp va boshqa)"
            ),
        }
    
    def __init__(self):
        self.config = loader.ModuleConfig(            
            loader.ConfigValue(
                "ADD_PHOTO",
                [
                    "https://te.legra.ph/file/4435c6047b6c7fa2392fb.jpg",
                    "https://te.legra.ph/file/5c67da79c87e4be1be9bf.jpg",
                    "https://te.legra.ph/file/65a901347c3722c7ad89d.jpg",                 ],
                lambda: self.strings("add_photo_tutorial"),
                validator=loader.validators.Series(validator=loader.validators.Link()),
            ),            
        )
    
    @loader.command(
        ru_doc=("Добавить кринж через конфигурацию")
        )
    async def addcringe(self, message):
        """Add cringe via configuration"""
        
        await self.allmodules.commands['config'](
        await utils.answer(message, f'{self.get_prefix()}config {self.strings("name")}'))
        return

    @loader.command(
        ru_doc=("Отправить случайный кринж")
        )
    async def cringe(self, message):
        """Send random cringe"""    
        reply = await message.get_reply_message()   
            
        cringe_list = self.config['ADD_PHOTO']
        
        cringe_random = (
            f"{random.choice(cringe_list)}"
            )
        
        await message.edit(self.strings('done'))  
        await message.delete()
        await message.client.send_file(
            message.to_id, 
            cringe_random, 
            reply_to=reply.id if reply else None)

