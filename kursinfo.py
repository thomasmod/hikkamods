__version__ = (1, 1, 0)

#            ▀█▀ █ █ █▀█ █▀▄▀█ ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀ █ █▀█ ▄█  
#             https://t.me/netuzb
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta desc: Browse movies by genre and watch them online via bot
# meta pic: https://te.legra.ph/file/9bc7500413b399da7298b.png
# meta banner: https://te.legra.ph/file/0191e8de52db3100da5b8.jpg
# meta developer: @wilsonmods
# scope: hikka_only
# scope: hikka_min 1.3.0

from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 

from asyncio.exceptions import TimeoutError 
from asyncio import sleep 
 
wilson_emoji = "🚨 "
 
class KursModMod(loader.Module): 
    """Information about course currency [optimization fully provided]""" 
    strings = {
               "name": "KursInfo",
               "wilson_pls_try_again": wilson_emoji + "<b>Please try again!</b>",
               "wilson_pls_write_course": wilson_emoji + "<b>Please enter the rate amount and currency.</b>",
               "wilson_error_method": wilson_emoji + "<b>An error was observed.</b>",
               "wilson_pls_delete_it": wilson_emoji + "<b>Activate the bot below - </b>@exchange_rates_vsk_bot"} 
               
    strings_ru = {
               "wilson_pls_try_again": wilson_emoji + "<b>Попробуй еще раз!</b>",
               "wilson_pls_write_course": wilson_emoji + "<b>Давай только с текстом?</b>",
               "wilson_error_method": wilson_emoji + "<b>Неизвестная ошибка!</b>",
               "wilson_pls_delete_it": wilson_emoji + "<b>Ты забыл активировать! - </b>@exchange_rates_vsk_bot"} 

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self._me = await client.get_me()
 
    async def kurscmd(self, message): 
        """> [amount (currency)] «example: .kurs 100 usd»""" 
        text = utils.get_args_raw(message) 
        kurs_net = f"👇 The <b>«{text}» course currency</b> is shown below."
        await message.edit(kurs_net)
        await sleep (10.0)
        await message.delete()
        try:
            text = utils.get_args_raw(message) 
            reply = await message.get_reply_message() 
            chat = "@exchange_rates_vsk_bot" 
            if not text and not reply: 
                await message.edit(self.strings("wilson_pls_write_course", message))                
                return 
            if text: 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=1210425892)) 
                        await message.client.send_message(chat, text) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply(self.strings("wilson_pls_delete_it", message))
                        return 
                    if not response.text: 
                        await message.edit(self.strings("wilson_pls_try_again", message))
                        return
                    await self.client.send_message(message.to_id, response.text)
                    await self.client.delete_dialog(chat) 
        except TimeoutError: 
            return await message.edit(self.strings("wilson_error_method", message))
            
