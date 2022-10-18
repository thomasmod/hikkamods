__version__ = (2, 2, 0)

#            ▀█▀ █ █ █▀█ █▀▄▀█ ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀ █ █▀█ ▄█  
#             https://t.me/netuzb
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta desc: Find music quickly and the quality is very high
# meta pic: https://te.legra.ph/file/c13bda4dc3eaa8c3f0f4e.png
# meta banner: https://te.legra.ph/file/0254e03843074fa879d2f.jpg
# meta developer: @wilsonmods

# scope: hikka_only
# scope: hikka_min 1.3.0

from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 
from asyncio.exceptions import TimeoutError 

# FORWARDING BOTS
vk_music = "vkmusbot"
spotify_music = "spotifysavebot"

# EMOJI PLACE 
em_violin = "🎻 "
em_agr = "😔 "
em_search = "🔍 "

@loader.tds
class MusicFinderMod(loader.Module):
    """Find music quickly and the quality is very high"""
    
    strings = {
        "name": em_violin + "MusicFinder",
        "music_not_found": em_agr + "<b>Nothing found!</b>",
        "music_searching": em_search + "<b>Wanted...</b>",
        "music_found": em_violin + "<i>Found!",
        "music_cant_find": em_agr + (
            "<b>No music found. Maybe you misspelled"
            " the name?</b>"
            ),
        }
        
    strings_ru = {
        "music_not_found": em_agr + "<b>Не найдено</b>",
        "music_searching": em_search + "<b>Ищем музыку...</b>",
        "music_found": em_violin + "<i>Найден!",
        "music_cant_find": em_agr + (
            "<b>Музыка не найдена.  Может быть, вы ошиблись"
            " в названии?</b>"
            ),
        }
    
    strings_uz = {
        "music_not_found": em_agr + "<b>Topilmadi</b>",
        "music_searching": em_search + "<b>Musiqa qidirilmoqda...</b>",
        "music_found": em_violin + "<i>Topildi!",
        "music_cant_find": em_agr + (
            "<b>Musiqa topilmadi, balkim siz"
            " nomini xato yozgandirsiz?</b>"
            ),
        }
    
    async def client_ready(self, client, db):
        self.client = client
        self._db = db
        self._me = await client.get_me()
        
    @loader.command(
        ru_doc = ("[название] - Введите, чтобы найти на Spotify")
    )
    async def sptdl(self, message):
        """[type] - to find on Spotify"""
        args = utils.get_args_raw(message)
        via = " | <a href='https://t.me/spotifysavebot'>spotify</a></i>"
        if not args:
            return 
            await message.edit(self.strings("music_not_found", message))

        message = await message.edit(self.strings("music_searching", message))
        try:
            message = message[0]
        except: pass
        music = await self.client.inline_query(spotify_music, args)
        for mus in music:
            if mus.result.type == 'audio':
                await self.client.send_file(
                    message.peer_id, 
                    mus.result.document, 
                    reply_to = message.reply_to_msg_id, 
                    caption = f"{self.strings('music_found')}{via}"
                )
                return await message.delete()
                return await message.edit(self.strings("music_cant_find", message))

    @loader.command(
        ru_doc = ("[название] - Введите, чтобы найти через VK")
    )
    async def vkdl(self, message): 
        """[type] - to find via VK""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message()
        via = " | <a href='https://t.me/vkmusbot'>vkmus</a></i>"
        if not args: 
            return await message.edit(self.strings("music_not_found", message))
        try: 
            await message.edit(self.strings("music_searching", message))
            music = await message.client.inline_query(vk_music, args) 
            await message.delete() 
            await message.client.send_file(
                message.to_id, 
                music[0].result.document, 
                caption = f"{self.strings('music_found')}{via}", 
                reply_to = reply.id if reply else None
            ) 
            
        except: return await message.client.send_message(
            message.chat_id, 
            f"<b>{args} not found</b>")
