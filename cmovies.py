__version__ = (1, 2, 0)

#            ▀█▀ █ █ █▀█ █▀▄▀█ ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀ █ █▀█ ▄█  
#             https://t.me/netuzb
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta desc: Browse movies by genre and watch them online via bot
# meta pic: https://te.legra.ph/file/386e8b541bb93f1537d1d.png
# meta banner: https://i.imgur.com/ccA9WkZ.jpeg
# meta developer: @wilsonmods
# scope: hikka_only
# scope: hikka_min 1.3.0
		
from asyncio import sleep
from ..inline.types import InlineCall

from telethon.tl.types import Message
from ..inline.types import InlineCall
from .. import loader, security, utils

link = "\n\n<b>Основатель</b>: <a href='t.me/netuzb'>Thomas Wilson</a>"
request = """<code>Название: (название фильма)
Жанр: (от одного до трех жанров)
Страны: (название страны)
Режиссёр: (Ф.И.О)
Длительность: (в минутах) мин.
КиноПоиск: (рейтинг)

Описание: (краткая информация о фильме)</code>

<b>🎨 Если возможно, ссылка на изображение баннера фильма (размер 1280x620) была бы отлично.</b>"""

@loader.tds
class CMovies(loader.Module):
    """Просмотр лучших фильмов, отсортированных по жанрам"""

    strings = {
		"name": "CMovies",
		"no": "🤷 <b>Этот каталог в настоящее время недоступен ни для одного фильма</b>\n🚨 Если вы хотите помочь нам добавить фильмы то пишите мне: <a href='t.me/netuzb'>Thomas Wilson</a>",
		"request_example": "⭐ <b>Спасибо за ваш интерес о подаче предложения</b>\n  – Очень просто, не сложно\n\n" + request,
		"main": "🎬 <b>My Movies</b> - модуль который поможет вам найти интересные фильмы",
		"fantastic": "🎬 <b>Научно-фантастика</b> - Здесь собраны все <a href='t.me/netuzb'>мои</a> избранные фильмы",
		"put": "🎬 <b>Путешествие</b> - Здесь собраны все <a href='t.me/netuzb'>мои</a> избранные фильмы",
		"ujas": "🎬 <b>Ужасы</b> - Здесь собраны все <a href='t.me/netuzb'>мои</a> избранные фильмы",
		"intr": "<b>Название: Интерстеллар (2014)\nЖанр: фантастика, драма, приключения\nСтраны: США, Великобритания, Канада\nРежиссёр: Кристофер Нолан\nМузыка: Ханс Циммер\nДлительность: 169 мин.\nКиноПоиск: 8,6\nIMDb: 8,6</b>" + link,
		"lucy": "<b>Название: Люси (2014)\nЖанр: боевик, фантастика\nСтрана: Франция\nРежиссёр: Люк Бессон\nМузыка: Эрик Серра\nДлительность: 89 мин.\nКиноПоиск: 6,7\nIMDb: 6,4</b>" + link,
		"nach": "<b>Название: Начало (2010)\nЖанр: фантастика, боевик, триллер, драма, детектив\nСтраны: США, Великобритания\nРежиссёр: Кристофер Нолан\nМузыка: Ханс Циммер\nДлительность: 148 мин.\nКиноПоиск: 8,7\nIMDb: 8,8</b>" + link,
		"kniga": "<b>Название: Книга Илая (2009)\nЖанр: боевик, драма\nВремя: 01:57\nРейтинг: КП 7.10 / IMDb 6.90\nСтрана: США\nРежиссер: Альберт Хьюз, Аллен Хьюз\nВ ролях: Дензел Вашингтон, Гари Олдман, Мила Кунис, Рэй Стивенсон, Дженнифер Билз, Малкольм МакДауэлл, Фрэнсис де ла Тур, Майкл Гэмбон, Том Уэйтс, Ивэн Джонс</b>" + link,
		"mars": "<b>Название: Книга Илая (2009)\nЖанр: приключения, фантастика\nВремя: 02:21\nРейтинг: КП 7.70 / IMDb 8.00\nСтрана: США, Великобритания\nРежиссер: Ридли Скотт\nВ ролях: Мэтт Дэймон, Джессика Честейн, Чиветель Эджиофор, Кристен Уиг, Джефф Дэниелс, Майкл Пенья, Шон Бин, Кейт Мара, Себастьян Стэн, Аксель Хенни</b>" + link,
		"voyna": "<b>Название: Война миров (2005)\nЖанр: драма, приключения\nВремя: 01:56\nРейтинг: КП 7.10 / IMDb 6.50\nСтрана: США\nРежиссер: Стивен Спилберг\nВ ролях: Том Круз, Дакота Фаннинг, Миранда Отто, Джастин Чэтвин, Тим Роббинс, Рик Гонсалес, Юл Васкес, Ленни Венито, Лиза Энн Уолтер, Энн Робинсон</b>" + link,
		"put_zem": "<b>Название: Путешествие к Центру Земли (2008)\nЖанр: боевик, приключения, семейный, фантастика, фэнтези\nРейтинг: 6.7\nОписание: Пытаясь узнать о судьбе исчезнувшего брата, учёный, его племянник и их проводница открывают фантастичный и опасный затерянный мир в центре Земли.</b>" + link,
		"put_jumanji": "<b>Название: Джуманджи: Новый уровень (2019)\nДата выхода: 12 декабря 2019 г. (РФ)\nЖанр: фэнтези, боевик, комедия, приключения\nСтрана: США\nРежиссёр: Джейк Кэздан\nМузыка: Генри Джекман\nДлительность: 123 мин.\nКиноПоиск: 6,7\nIMDb: 6,9\n\nОписание: Чтобы спасти одного из приятелей, остальным приходится вернуться в игру. К их удивлению, правила Джуманджи изменились, и все идет наперекосяк. Чтобы выжить друзьям предстоит отправиться в путешествие по самым неизведанным и таинственным уголкам игры – от засушливой пустыни до заснеженных гор.</b>" + link,
		"ujas_astral": "<b>Название: Астрал (2010)\nЖанр: триллер, ужасы\nРейтинг: 6.8\n\nОписание: Джош и Рене переезжают с детьми в новый дом, но не успевают толком распаковать вещи, как начинаются странные события. Необъяснимо перемещаются предметы, в детской звучат странные звуки… Но настоящий кошмар начинается для родителей, когда их десятилетний сын Далтон впадает в кому. Все усилия врачей в больнице помочь мальчику безуспешны.</b>" + link,
		"ujas_astral2": "<b>Название: Астрал: Глава 2 (2013)\nЖанр: ужасы, триллер\nСтраны: США, Канада\nРежиссёр: Джеймс Ван\nМузыка: Джозеф Бишара\nДлительность: 110 мин.\nКиноПоиск: 6,5\nIMDb: 6,6\n\nОписание: Семья Ламберт стремится раскрыть тайну, из-за которой они оказались в опасной связи с миром духов. Семейство переезжает в дом матери Джоша, но, как оказывается, туда вселяются не только они. Путешествие в мир призраков не прошло для семьи Ламберт бесследно — вместе с Джошем в мир людей проник дух, который вновь хочет быть живым. И вскоре в доме снова начинают происходить странные и страшные вещи.</b>" + link,
		"ujas_astral3": "<b>Название: Астрал: Глава 3 (2015)\nЖанр: ужасы, триллер, детектив\nСтраны: Канада, Великобритания, США\nРежиссёр: Ли Уоннелл\nМузыка: Джозеф Бишара\nДлительность: 97 мин.\nКиноПоиск: 5,8\nIMDb: 6,1\n\nОписание: История о том, как одаренный экстрасенс Элис Рейнер неохотно соглашается использовать свои способности для установления связи с мертвыми, чтобы помочь девочке-подростку, которая стала мишенью для опасной сверхъестественной сущности.</b>" + link,
		"ujas_astral4": "<b>Название: Астрал 4: Последний ключ (2018)\nЖанр: ужасы, триллер, детектив\nСтраны: Канада, США\nРежиссёр: Адам Робител\nМузыка: Джозеф Бишара\nДлительность: 103 мин.\nКиноПоиск: 5,5\nIMDb: 5,7\n\nОписание: Новая глава истории об экстрасенсе, которая умеет разговаривать с мёртвыми. Детство Элизы было трудным - жестокий отец считал, что девочка придумывает истории о потустороннем, поэтому бил её и запирал в подвале. Однажды, сидя в тёмном подвале, Элиза начинает общаться с коварным призраком, который убеждает её открыть дверь. Вырвавшееся наружу зло тут же убивает мать девочки. Много лет спустя Элиза всё ещё пытается восстановить в памяти события той ужасной ночи, когда получает просьбу о помощи. Мужчину одолели призраки, и живёт он в том самом доме, где прошло детство Элизы.</b>" + link,
                "bobrovi": "<b>Название: Последний богатырь\nЖанр: Фантастика\nСтраны: Россия\nРежиссёр: Дмитрий Дьяченко\nДлительность: 108 мин.\nКиноПоиск: 6,7/10\n\nОписание: Главный герой, Иван Найдёнов (Виктор Хориняк) живёт в Москве. С материальной точки зрения Иван живёт неплохо — под именем «белый маг Светозар» он участвует в телешоу «Битва магов», ведёт частный приём состоятельных клиенток, имеет квартиру в Москва-Сити, но он очень одинок. Иван — сирота, воспитывался в детдоме, он холост, и никого из близких у него нет; единственный человек, с которым он общается более или менее регулярно — ворчливая приходящая домработница Галина.</b>" + link,
		"fantastic_button": "🔥 Фантастика",
		"put_button": "🌴 Путешествие",
		"horror_button": "🧟‍♀️ Ужасы",
		"comedy_button": "🎭 Комедия",
		"detective_button": "🕵️ Детектив",
		"drama_button": "💌 Драма",
		"x": "🔻 Закрыть",
		"request_to_me": "↗️ Подать заявку",
		"back": "↩️ Назад",
		"watch": "💾 Смотреть онлайн",
		}
		
    async def cmoviescmd(self, message):
           """> Посмотреть каталог фильмов"""
           await self.inline.form(
                    text = f"{self.strings('main')}",
                    reply_markup=[
                    [{
                            "text": self.strings('fantastic_button'),
                            "callback": self.fantastic
                    },
                    {
                            "text": self.strings('put_button'),
                            "callback": self.put
                    }],
                    [{
                            "text": self.strings('horror_button'),
                            "callback": self.ujas
                    },
                    {
                            "text": self.strings('drama_button'),
                            "callback": self.no
                    }],
                    [{
                            "text": self.strings('comedy_button'),
                            "callback": self.no
                    },
                    {
                            "text": self.strings('detective_button'),
                            "callback": self.no
                    }],
                    [{
                        "text": self.strings("x"), 
                        "action": "close"
                    }]], 
                        **{"photo": "https://raw.githubusercontent.com/Netuzb/umod_mods/main/mymovies.jpg"},
                    message=message,
                )                              
    
    async def main(self, call: InlineCall) -> None:
           await call.edit(
            text = f"{self.strings('main')}",
            reply_markup=[
                [{
                        "text": self.strings('fantastic_button'),
                        "callback": self.fantastic
                },
                {
                        "text": self.strings('put_button'),
                        "callback": self.put
                }],                
                [{
                        "text": self.strings('horror_button'),
                        "callback": self.ujas
                },
                {
                        "text": self.strings('drama_button'),
                        "callback": self.no
                }],
                [{
                        "text": self.strings('comedy_button'),
                        "callback": self.no
                },
                {
                        "text": self.strings('detective_button'),
                        "callback": self.no
                }],
                [{
                    "text": self.strings("x"), 
                    "action": "close"
                }]],   
                    **{"photo": "https://raw.githubusercontent.com/Netuzb/umod_mods/main/mymovies.jpg"},
                )

    async def no(self, call: InlineCall) -> None:
           await call.edit(
            text = f"{self.strings('no')}",
            reply_markup=[       
                [{
                    "text": self.strings("back"), 
                    "callback": self.main
                },{
                    "text": self.strings("x"), 
                    "action": "close"
                }]],   
                    **{"photo": "https://t.me/anonyusa/127"},
                )
                
    async def creqcmd(self, message):
           """> Информация о добавлении предложения фильма"""
           await self.inline.form(
                    text = f"{self.strings('request_example')}",
                    reply_markup=[
                    [{
                            "text": self.strings('request_to_me'),
                            "url": "https://t.me/netuzb",
                    }],
                    [{
                        "text": self.strings("x"), 
                        "action": "close"
                    }]], 
                        **{"photo": "https://t.me/anonyusa/131"},
                    message=message,
                )                                         
                
                
    # ФАНТАСТИКА / Thomas Wilson
    # ФАНТАСТИКА / Thomas Wilson
    # ФАНТАСТИКА / Thomas Wilson

    async def fantastic(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('fantastic')}",
		    reply_markup=[
                [{
                        "text": "Люси (2014)", 
                        "callback": self.lucy
                },{
                        "text": "Интерстеллар (2014)", 
                        "callback": self.intr
                }],
                [{      
                        "text": "Начало (2010)", 
                        "callback": self.nach
                },{
                        "text": "Книга Илая (2009)", 
                        "callback": self.kniga
                }],
                [{
                        "text": "Марсианин (2015)", 
                        "callback": self.mars
                },{
                        "text": "Война миров (2005)", 
                        "callback": self.voyna
                }],
                [{
                        "text": "Последний богатырь (2017)", 
                        "callback": self.bobrovi
                }],
                [{
                    "text": self.strings("back"), 
                    "callback": self.main
                },{
                    "text": self.strings("x"), 
                    "action": "close"
                }]], 
                    **{"photo": "https://raw.githubusercontent.com/Netuzb/umod_mods/main/mymovies.jpg"},
                )                                            
                
    async def lucy(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('lucy')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.fantastic
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/115"},
                )
    
    async def intr(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('intr')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.fantastic
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/118"},
                )
    
    async def nach(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('nach')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.fantastic
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/119"},
                )
    
    async def kniga(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('kniga')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.fantastic
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/120"},
                )
    
    async def mars(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('mars')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.fantastic
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/121"},
                )
                
    async def voyna(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('voyna')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.fantastic
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/122"},
                )

    async def bobrovi(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('bobrovi')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.fantastic
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/132"},
                )

                
                
    # ПУТЕШЕСТВИЕ / Thomas Wilson 
    # ПУТЕШЕСТВИЕ / Thomas Wilson 
    # ПУТЕШЕСТВИЕ / Thomas Wilson                
                
    async def put(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('put')}",
		    reply_markup=[
                [{
                        "text": "Путешествие к Центру Земли (2008)", 
                        "callback": self.put_zem
                }],
                [{
                        "text": "Джуманджи: Новый Уровень (2019)", 
                        "callback": self.put_jumanji
                }],
                [{
                    "text": self.strings("back"), 
                    "callback": self.main
                },{
                    "text": self.strings("x"), 
                    "action": "close"
                }]], 
                    **{"photo": "https://raw.githubusercontent.com/Netuzb/umod_mods/main/mymovies.jpg"},
                )
    
    async def put_zem(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('put_zem')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.put
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/123"},
                )
    
    async def put_jumanji(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('put_jumanji')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.put
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/125"},
                )
                
                
                
    # УЖАСЫ / Thomas Wilson 
    # УЖАСЫ / Thomas Wilson 
    # УЖАСЫ / Thomas Wilson                
                
    async def ujas(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('ujas')}",
		    reply_markup=[
                [{
                        "text": "Астрал (2010)", 
                        "callback": self.ujas_astral
                }],
                [{
                        "text": "Астрал: Глава 2 (2013)", 
                        "callback": self.ujas_astral2
                }],
                [{
                        "text": "Астрал: Глава 3 (2015)", 
                        "callback": self.ujas_astral3
                }],
                [{
                        "text": "Астрал 4: Последний ключ (2018)", 
                        "callback": self.ujas_astral4
                }],
                [{
                    "text": self.strings("back"), 
                    "callback": self.main
                },{
                    "text": self.strings("x"), 
                    "action": "close"
                }]], 
                    **{"photo": "https://raw.githubusercontent.com/Netuzb/umod_mods/main/mymovies.jpg"},
                )
    
    async def ujas_astral(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('ujas_astral')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.ujas
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/126"},
                )
    
    async def ujas_astral2(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('ujas_astral2')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.ujas
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/128"},
                )
    
    async def ujas_astral3(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('ujas_astral3')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.ujas
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/129"},
                )
    
    async def ujas_astral4(self, call: InlineCall):
           await call.edit(
            text = f"{self.strings('ujas_astral4')}",
		    reply_markup=[
                [{
                        "text": self.strings('back'), 
                        "callback": self.ujas
                },
                {
                        "text": self.strings('watch'), 
                        "url": "https://t.me/HDFilmsBot"
                }]], 
                    **{"photo": "https://t.me/anonyusa/130"},
                )
