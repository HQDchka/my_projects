import telebot, random, requests
from telebot import types

bot = telebot.TeleBot('Token')

@bot.message_handler(commands=['help','start'])
def start(message):
    bot.send_message(message.chat.id, f'Чтобы узнать погоду напиши Погода (название города)\nНапример: "Погода Орёл"')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Стикеры")
    btn2 = types.KeyboardButton("Мой создательℹ")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Что ты хочешь?", reply_markup=markup)

@bot.message_handler(regexp='Мой создательℹ')
def creator(message):
    bot.send_message(message.chat.id,'17 лет\nTelegram:@HQD_Daniil\nDiscord:.hqd.\nSteam: https://steamcommunity.com/profiles/76561199052437320/')

@bot.message_handler(regexp='Стикеры')
def stickers(message):
    stickers=[SOME_STICKERS]
    bot.send_sticker(message.chat.id,stickers[random.randint(0,2)])

@bot.message_handler(regexp='Погода')
def weather(message):
    API_key = "API"
    f = f'https://api.openweathermap.org/data/2.5/weather?&q={message.text.split()[1]}&lang=ru&units=metric&appid={API_key}'
    weather = requests.get(f).json()
    temp = round(weather['main']['temp'])
    sky = (weather['weather'][0]['description'])
    wind_deg = round(weather['wind']['deg'])
    humidity = weather['main']['humidity']
    if 45 < wind_deg <= 135:
        wd = 'Восточный'
    if 135 < wind_deg <= 225:
        wd = 'Южный'
    if 225 < wind_deg <= 315:
        wd = 'Западный'
    if 315 <= wind_deg or wind_deg <= 45:
        wd = 'Северный'
    wind_speed = (weather['wind']['speed'])
    bot.send_message(message.chat.id,f'Город: {message.text.split()[1]}\nПогода: {sky}\nТемпература: {temp}°С\nНаправление ветра: {wind_deg}°({wd} ветер)\nСкорость ветра: {wind_speed}м/с\nВлажность {humidity}%')

@bot.message_handler(regexp='Умиротворения')
def river(message):
    bot.send_message(message.chat.id, 'Я в своем познании настолько преисполнился, что я как будто бы уже сто триллионов миллиардов лет проживаю на триллионах и триллионах таких же планет, как эта Земля, мне этот мир абсолютно понятен, и я здесь ищу только одного - покоя, умиротворения и вот этой гармонии, от слияния с бесконечно вечным, от созерцания великого фрактального подобия и от вот этого замечательного всеединства существа, бесконечно вечного, куда ни посмотри, хоть вглубь - бесконечно малое, хоть ввысь - бесконечное большое, понимаешь? А ты мне опять со своим вот этим, иди суетись дальше, это твоё распределение, это твой путь и твой горизонт познания и ощущения твоей природы, он несоизмеримо мелок по сравнению с моим, понимаешь? Я как будто бы уже давно глубокий старец, бессмертный, ну или там уже почти бессмертный, который на этой планете от её самого зарождения, ещё когда только Солнце только-только сформировалось как звезда, и вот это газопылевое облако, вот, после взрыва, Солнца, когда оно вспыхнуло, как звезда, начало формировать вот эти коацерваты, планеты, понимаешь, я на этой Земле уже как будто почти пять миллиардов лет живу и знаю её вдоль и поперёк этот весь мир, а ты мне какие-то... мне не важно на твои тачки, на твои яхты, на твои квартиры, там, на твоё благо. Я был на этой планете бесконечным множеством, и круче Цезаря, и круче Гитлера, и круче всех великих, понимаешь, был, а где-то был конченым говном, ещё хуже, чем здесь. Я множество этих состояний чувствую. Где-то я был больше подобен растению, где-то я больше был подобен птице, там, червю, где-то был просто сгусток камня, это всё есть душа, понимаешь? Она имеет грани подобия совершенно многообразные, бесконечное множество. Но тебе этого не понять, поэтому ты езжай себе , мы в этом мире как бы живем разными ощущениями и разными стремлениями, соответственно, разное наше и место, разное и наше распределение. Тебе я желаю все самые крутые тачки чтоб были у тебя, и все самые лучше самки, если мало идей, обращайся ко мне, я тебе на каждую твою идею предложу сотню триллионов, как всё делать. Ну а я всё, я иду как глубокий старец,узревший вечное, прикоснувшийся к Божественному, сам стал богоподобен и устремлен в это бесконечное, и который в умиротворении, покое, гармонии, благодати, в этом сокровенном блаженстве пребывает, вовлеченный во всё и во вся, понимаешь, вот и всё, в этом наша разница. Так что я иду любоваться мирозданием, а ты идёшь преисполняться в ГРАНЯХ каких-то, вот и вся разница, понимаешь, ты не зришь это вечное бесконечное, оно тебе не нужно. Ну зато ты, так сказать, более активен, как вот этот дятел долбящий, или муравей, который очень активен в своей стезе, поэтому давай, наши пути здесь, конечно, имеют грани подобия, потому что всё едино, но я-то тебя прекрасно понимаю, а вот ты меня - вряд ли, потому что я как бы тебя в себе содержу, всю твою природу, она составляет одну маленькую там песчиночку, от того что есть во мне, вот и всё, поэтому давай, ступай, езжай, а я пошел наслаждаться прекрасным осенним закатом на берегу теплой южной реки. Всё, ступай, и я пойду.')

bot.polling(none_stop=True)
