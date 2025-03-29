# Вы можете расположить сценарий своей игры в этом файле.
define alph = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю '
# Определение персонажей игры.
define ii = Character('{glitch=3}42{/glitch}', color="#4B0082", what_color="#898989", what_prefix = "{cps=60}", what_suffix = "{/cps}")
define unknow = Character('???', color="#222290", what_prefix = "{cps=40}", what_suffix = "{/cps}")
define character_forChoise1 = Character('[ggname]', what_prefix = "{cps=50}", what_suffix = "{/cps}")
define character_forChoise2 = Character('[ggname]', what_prefix = "{cps=50}", what_suffix = "{/cps}")
define tr = Character('Терминал', color="#646464", what_color="#a3a3a3",  what_prefix = "{cps=50}", what_suffix = "{/cps}")
define mod = Character('{glitch=20}Modeus{/glitch}', what_color="#cc9830",  what_prefix = "{cps=50}", what_suffix = "{/cps}")
# для починенного модеуса
define modn = Character('Modeus', color="#d29e04", what_color="#cc9830",  what_prefix = "{cps=50}", what_suffix = "{/cps}")
# для угадывания пароля в виде режима nvl (gg и windows)
define win = Character('Terminal27', color="#0ead3e", what_color="#0ead3e",  what_prefix = "{cps=50}", what_suffix = "{/cps}", kind=nvl)
define ii_nvl = Character('{glitch=3}42{/glitch}', color="#4B0082", what_color="#0ead3e",  what_prefix = "{cps=50}", what_suffix = "{/cps}", kind=nvl)
define gl = Character(name="{glitch=66}GLITCH{/glitch}", what_prefix = "{cps=80}{glitch=15}", what_suffix = "{/glitch}{/cps}" )

define gnw = Character('[ggname]', what_prefix = "{cps=50}", what_suffix = "{/cps}", kind=nvl)

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 10
    yoffset 0
    repeat 1

default gg = None
$ gg_gender = None
define gg_image = None
init python:
    def set_images():
        global gg_image
        if gg_gender == 'male':
            gg_image = 'images/male_gg_normal.png'
        else:
            gg_image = 'images/female_gg_normal.png'

define female_gg_idle = "images/female_gg_idle.png"
define female_gg_hover = "images/female_gg_hover.png"
define male_gg_idle = "images/male_gg_idle.png"
define male_gg_hover = "images/male_gg_idle.png"

define hover_sound = "audio/sound_hover.mp3"

# Игра начинается здесь:
label start:

    if gg is None:
        call screen character_selection with fade

    $ set_images()

    $ ggname = renpy.input("{glitch=15}Как тебя зовут, путник?{/glitch}", length=16, allow=alph)
    define gg = Character("[ggname]")

    jump prolog

# Сюжет после выбора пола
label prolog:
    play music "start.mp3"
    scene prolog2 with fade:
        zoom 1.5
    unknow "[ggname], здравствуй.."
    unknow ```Мир пошел по пути глобальной цифровизации,
            человек всё больше окружал себя технологиями.
            И вот произошел большой скачок в истории:
            инженеры и программисты смогли создать виртуальный мир,
            где могли находится миллионы аватаров людей```
    unknow "В виртуальном мире всё стало проще:
            люди могут удалённо работать, учиться и играть"
    unknow "Технологии настолько сильно развились,
        что виртуальный мир почти полностью заменил людям реальность"
    unknow "Чтобы управлять этим миром, были созданы программы
        - множество искусственных интеллектов,
            которые выполняли свои задачи"
    unknow "Но доступ к программам, есть только у разработчиков"
    unknow "Найдя лазейку в коде, вы попадаете в неизвестный мир искусственного интеллекта,
        где вам ничего неизвестно..."
    stop music

    scene hole with fade:
        zoom 1.0 xalign 0.6 yalign 0.3
        linear 5 zoom 1.5
    play sound "sound-fall.mp3"
    $ renpy.pause(3.0)

    scene black with fade
    gg "Чёрт.. Кажется, я куда-то упал"
    gg "Как же болит голова"
    gg "И где это я?"

    scene matrix-veryhd with fade
    play music "music-new_world.mp3"
    gg "Я что попал в код?!"

    ii "Ого.. Не думал, что здесь ещё кто-нибудь окажется"
    gg "ААА!! Это ещё что за голос?!"
    show 42 at bounce, center with dissolve
    ii "Добро пожаловать в мой мир - мир цифр и логики!
        Здесь всё не так, как ты привык"
    gg "Что?? Кто ты такой?!"
    show 42 at bounce, center
    ii "Я всего лишь набор нулей и единиц, как и ты в этом мире"
    gg "Но.. Как ты смог сюда попасть,
        это же закрытая сторона для обычных пользователей"
    show 42 at bounce, center
    ii "Не думал, что ты такой наивный. Не ты первый, не ты последний,
        кто нашёл лазейку"
    gg "То есть сюда кто-то попадает?"
    show 42 at bounce, center
    ii "Именно"
    show 42 at bounce, center
    ii "Каждый приходит сюда со своими целями и желаниями.
        И в начале они всегда встречают меня"
    gg "Дак ты сможешь мне помочь?"
    show 42 at bounce, center
    ii "ХаХах4хаХах0х4"
    show 42 at bounce, center
    ii "Конечно нет. Думал всё так просто?
        Я не могу дать то, что ты хочешь, но могу направить"


    $ first_choice = 0
    menu:
        ii "Скажи, с какой целью ты пришёл сюда?"
        "{color=#98FB98}Я пришёл сюда, чтобы найти уязвимости системы
            и исправить их{/color}":
                $ first_choice = "good"
        "{color=#DC143C}Я хочу взломать систему изнутри, чтобы обрести власть над
            этим миром{/color}":
                $ first_choice = "bad"

    show 42 at bounce, center
    ii "Что ж... Теперь я понял твои намерения"
    show 42 at bounce, center
    ii "Начни свой путь вон с той комнаты. Удачи!"
    hide 42 with dissolve

    gg "Стой! Но... {w=0.5}куда он делся?"

    gg "Не мог просто мне помочь сразу, а не пропадать непонятно куда?!"

    scene road-phone with fade

    menu:
        "Продолжить путь":
            jump action_after_fm_with42
        "Вернуться обратно":
            jump first_end

label first_end:

    show 42 at center

    menu:
        ii "Ты точно хочешь уйти?"
        "Нет...Всё-таки я хочу продолжить путь":
            jump action_after_fm_with42
        "Да":
            ii "И все же.. {w=0.2} Ты оказался не таким смелым"
            scene black with fade
            unknow "The end.."
            jump the_end


label action_after_fm_with42:

    scene black with fade
    #ПОМЕНЯТЬ
    gg "Кажется, впереди есть помещение, похожее на.."
    # картинки говно, да и дизайнер не скинул, поэтому пока так
    scene room-terminal with dissolve:
        zoom 1.5 xalign 0.4 yalign 0.2
    gg "Комнату?"
    gg "Это что, терминал? {w=0.6}Он выглядит поломанным"

    scene room with fade
    show terminal at bounce, left with dissolve:
        yalign -0.3
        zoom 1.0
        linear 0.3 zoom 1.1
    tr "Приветствую тебя, пользователь. Терминал готов с исполнению."
    show terminal at left:
        yalign 2.7
        zoom 1.1
        linear 0.3 zoom 1.0
    show 42 at bounce, right with dissolve:
        ypos 1500
        xpos 1500
        zoom 1.2
        linear 0.3 zoom 1.0

    ii "Оо... {w=0.3}ты наконец нашел моего старого друга"
    gg "Да хватит приходить из неоткуда!"
    show 42 at bounce, right with dissolve:
        ypos 1400
        xpos 1500
        linear 0.3 zoom 1.15
    ii "Я тоже рад тебя видеть!"
    show 42 at bounce, right:
        ypos 1400
        xpos 1500
    ii "В начале пути тебе надо определить, где искать уязвимости системы"
    show 42 at bounce, right:
        ypos 1400
        xpos 1500
    ii "Здесь каждая программа обладает своим IP-адресом, по которому можно её отследить"
    show 42 at bounce, right:
        ypos 1400
        xpos 1500
    ii "Всё как в реальной жизни: Твой IP-адрес очень важен для отправки и получения информации через Интернет"
    show 42 at bounce, right:
        ypos 1400
        xpos 1500
    ii "Но если хакеры узнают твой IP-адрес, они могут использовать его для получения ценной информации, включая твоё местоположение и сетевую идентификацию"
    gg "Значит надо найти нужный ip-адрес"

    show 42 at right:
        ypos 1400
        xpos 1500
        linear 0.3 zoom 1.15
    show terminal at bounce, left with dissolve:
        yalign -0.2
        zoom 1.1
        linear 0.3 zoom 1.3
    scene tv with fade
    tr "Введите команду"
    define command = None
    $ command = renpy.input("{glitch=4}Введите команду{/glitch}", length=8)
    if command != "arp -a" or command != "ARP -A":
        $ frase = "Введите arp -a"
        $ count_fault = 0
        while command != 'arp -a':
            if count_fault >= 2:
                $ frase = "{glitch=20}ДА ВВЕДИ ТЫ УЖЕ ARP -A{/glitch}"
            $ command = renpy.input("{glitch=4}[frase]{/glitch}", length=8)
            if command == "arp -a" or command == "ARP -A":
                jump ip_choice
            $ count_fault += 1
    else:
        jump mini_1

init python:
    ips = [
        {"address": "192.168.1.100", "correct": False},
        {"address": "10.0.0.5", "correct": False},
        {"address": "8.8.8.8", "correct": False},
        {"address": "192.67.213.2", "correct": False},
        {"address": "56.123.2.144", "correct": False},
        {"address": "192.233.23.3", "correct": False},
        {"address": "132.2.0.0", "correct": False},
        {"address": "8.2.3.5", "correct": False},
        {"address": "{glitch=40}172.16.25.12{/glitch}", "correct": True},
        {"address": "{glitch=3}27.1828....{/glitch}", "correct": False, "hint": "   {color=#03590c}*psswrd{/color}"},
        {"address": "1828.....", "correct": False},
    ]

    def is_valid_ip(address):
        parts = address.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            try:
                num = int(part)
                if not (0 <= num <= 255):
                    return False
            except ValueError:
                return False
        return True

screen ip_selection:
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "Подозрительный диапазон IP-адресов"
            for ip in ips:
                hbox:
                    textbutton ip["address"] action [If(ip["correct"], Return("correct_ip"), Return("wrong_ip")),
                                                    If(ip["address"] == "{glitch=3}27.1828....{/glitch}", Return("hiden_ip"))]
                    if "hint" in ip:
                        text ip["hint"] xsize 300


label ip_choice:
    hide 42
    show screen ip_selection
    $ result = ui.interact()
    hide screen ip_selection
    if result == "correct_ip":
        play sound "sound_selected.mp3"
        jump after_mini_1
    elif result == "hiden_ip":
        jump after_find_password_ip
    else:
        "Вы нажали неправильный IP-адрес. Попробуйте снова."
        jump ip_choice


#в промежутке должна быть миниигра, затем снова часть диалога, либо она будет в самой игре
pause 2.0
# после миниигры
label after_find_password_ip:
    show screen ip_selection
    gg "Что это за странная строка?"
    show 42 at bounce, right:
        ypos 1500
        xpos 1630
        zoom 1.2
        linear 0.3 zoom 1.0
    ii "Лучше не связывайся с этим. Это остатки вредоносного ПО"
    show 42 at bounce, right:
        ypos 1500
        xpos 1630
    ii "{glitch=5}Странно, что он ещё остался жив. Надо будет разобраться с ним...{/glitch}"
    jump ip_choice

screen net_prav:
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "{w=0.4}Доступ запрещен. {w=0.2}Недостаточно прав"

screen nado_password:
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "{w=0.4}Введите пароль администратора\n         **********"

label after_mini_1:
    scene tv
    gg "Ура! Смотри я нашел нужный... {w=1.5}Ему видимо доставляет удовольствие постоянно пропадать."
    gg "Покажи расположение программы по адресу 172.16.25.12"
    show screen net_prav
    gg "Когда у человека стало меньше прав, чем у машины?"
    hide screen net_prav
    show screen nado_password
    gg 'И откуда я узнаю пароль...'
    gg "Хм. Пароль состоит лишь из 10 цифр. Можно же его легко перебрать"

    hide screen nado_password
    jump passw

label passw:

    # ПАРОЛЬНЫЙ МАСТЕР можно наверное просто развернуть ее не как мини игру, а просто в виде NVL с подскаками...
    # define nvl = $ password = renpy.input("{glitch=4}Введите пароль{/glitch}", length=10)
    win ""
    screen input:

        window:

            style "nvl_window"
            text prompt xalign 0.5 yalign 0.4
            input id "input" xalign 0.5 yalign 0.5 color "#21d544"

        use quick_menu

    screen input_pass:
        frame:
            xalign 0.5
            yalign 0.4
            window:
                xsize 300
                ysize 250
                xalign 0.5
                style "nvl_window"
                text prompt xalign 0.5 yalign 0.4
                input id "input_pass" xalign 0.5 yalign 0.7 color "#21d544" length 10 allow "0123456789"




    $ cnt = 0
    $ ans = ""
    while ans != "2718281828":
        while ans != "2718281828":
            if cnt == 5:
                ii_nvl "Попробуй начать с ID терминала и дальше дата рождения {glitch=50}ЛЬ8А 70LCT0G0{/glitch} * 2"
            if cnt == 8:
                ii_nvl  "{glitch=10}Кажется, что-то ограничивает формат сообщений, который я могу передать. \nID терминала должно быть рядом с его именем{/glitch}"
            if cnt == 10:
                ii_nvl "ID + date * 2. Не забывай как работает умножение string type"

            $ ans = renpy.call_screen("input_pass", prompt="Введите пароль")
            $ cnt += 1
    if ans == "2718281828":
        gg "Ну, спасибо подсказкам пароля Windows"
        gg "И как этот странный человек смог войти в систему терминала?"

label after_mini_2:

    scene room with fade
    # хочется какой-то анимации падения небольшой, когда чел приземляется, анимацию bonce на сцену
    show terminal at bounce with dissolve:
        xalign 0.0
        yalign 1.0
    tr "Пароль верный, добро пожаловать, разработчик."
    gg "Это оказалось не так просто, если бы пароль состоял не только из цифр, то я бы очень долго его искал"
    gg "Терминал, покажи расположение программы по адресу 172.16.25.12"
    show terminal at bounce:
        xalign 0.0
        yalign 1.0
    tr "https://urfu.modeus.org"
    gg "Ну пора в дорогу"
    scene black with fade
    play sound "sound-fall.mp3"
    # Темный экран
    # Перемещаемся в другую локацию
    # игрок идёт и проваливается на этаж ниже
    gg "ААААаа!! {w=0.2}Куда я снова провалился!?"
    # происходит удачное приземление
    gg "Что за умник написал здесь код с такими дырами!?"
    play music "music-new_world.mp3"
    # *игрок видит рядом с собой тело, которое лежит уже давно, и оно явно так же упало сюда, но неудачно
    scene room-modeus with fade
    gg "Эй{w=0.5}, ты живой?"
    gg "Аууу? {w=0.8}Кажется, ему совсем плохо"
    scene server
    show modeus at bounce, left with moveinleft
    # слишком большой, нет?
    mod "{glitch=20}К сожалению нет...{/glitch}"
    gg "Ты же Модеус?{w=0.2} Я как раз тебя искал"
    gg "Что с тобой произошло"
    show modeus at bounce, left
    mod "{glitch=20}Да, ты смог меня найти{/glitch}"
    show modeus at bounce, left
    mod "{glitch=15}Но как видишь упал и не могу встать уже давно{/glitch}"
    show modeus at bounce, left
    mod "{glitch=15}Сначала большой наплыв студентов, потом DDos-атаки. Мои создатели явно плохо продумали средства защиты против этого всего{/glitch}"
    show modeus at bounce, left
    mod "{glitch=15}Слабая защита, неоптимизированный код, плохие сервера - всё это мешает мне стабильно работать{/glitch}"
    gg "Я как раз пришел помочь тебе с твоей проблемой!"
    gg "Сейчас я изменю твой код и подниму тебя наконец"


label after_mini_3:
    scene black with fade
    #show happy modeus
    show modeus-happy at bounce, center
    modn "Как же хорошо снова быть в строю"
    show modeus-smile at bounce, center
    modn "Спасибо, что залатал дыры в коде"
    gg "Без проблем, главное не падай больше"
    gg "Только помоги теперь мне выбраться обр..."
    hide modeus-smile
    show modeus-happy at bounce, center:
        zoom 1
        linear 1 zoom 1.3
    pause 2
    # на этаже выше слышны странные звуки
    modn "Пригнись, это Glitch сверху идёт"
    gg "Что он здесь ищет?"
    show modeus-happy at bounce, center:
        zoom 1.3
    modn "Из-за его атак я и попал сюда. Он ищет уязвимости и ломает программы изнутри"
    show modeus-happy at bounce, center:
        zoom 1.3
        linear 1 zoom 1.0
    modn "Вроде ушел"
    show modeus-happy at bounce, center:
        zoom 1.0
    modn "Пошли, я проведу нас обратно наверх"

    # игрок и модеус выбираются наверх
    scene black with fade
    hide modeus-happy
    show modeus-smile at bounce:
        xalign 0.0
    modn "Иди теперь обратно аккуратней, потому что Glitch может вернуться"
    hide modeus-smile
    show modeus-happy at bounce, left with dissolve:
        zoom 1.0 xalign 1.0 yalign 1.0
        linear 0.5 zoom 0.9

    # сцена с терминалом
    scene room with fade
    show terminal at bounce, center with dissolve:
        yalign 0.0
        zoom 1.0
        linear 0.3 zoom 1.1
    gg "Вроде здесь безопасно теперь"
    tr "У вас новое сообщение.{w=1} У вас новое сообщение.{w=1} У вас новое сообщение."
    gg "Удивительно, что здесь можно получать сообщения как по почте"
    # сцена с изображением сообщений (вот бы как в итисе задания сделать), там есть похожая хуйня
    # можно прям оттуда за основу взять, либо оформить число в виде картинок сцены и кнопок как при игре поиск предметов
    # доделай с концовками пж и играми, я возьму визуал и картинки
    jump minigame_4

init python:
    messages = [
        {
            "from": "Zandex",
            "title": "Стажировка",
            "message": "Открылась новая стажировка! Скорее заполняй заявку: http://zandex.ru/future-junior/anketa",
            "is_fishing": False},
        {
            "from": "English Club",
            "title": "Авторизуйся через соц.сети в 2 клика",
            "message": "Присоединяйся к кружку по английскому языку. englishclu8.xyz",
            "is_fishing": True},
        {
            "from": "FutureMessages",
            "title": "ПРЕДУПРЕЖДЕНИЕ!",
            "message": "Ваш сервер был взломан, чтобы обезопасить данные, подтвердите личность: http://neobman.org/tochnonevzlom",
            "is_fishing": True},
        {
            "from": "Modeus",
            "title": "От Modeus'a :)",
            "message": "Спасибо тебе ещё раз, что помог мне снова заработать.\n"
            "Теперь студенты без проблем смогут выбирать себе расписание занятий, а в деканат будет поступать меньше жалоб на меня. Остерегайся Глитча, он ищет таких как ты! Возьми этот дешифровщик он поможет тебе в битве с ним",
            "is_fishing": False},
        {
            "from": "42",
            "title": "{glitch=5}Посмотри, как освободишься{/glitch}",
            "message": "Привет, давно не виделись. Надеюсь, ты достиг своей цели и всё такое, но… Мне пришлось тебя покинуть, потому что Glitch стал охотиться на тебя.\n"
                "Ему нужны люди из реального мира, так он становится сильнее, поглощая их знания. Если ты читаешь это письмо, то ты пока в безопасности.\n"
                "Советую тебя быстрее уходить от сюда, но всё всегда остаётся в твоих руках. Я задержал его ненадолго, но это не вечно.\n"
                "При встрече с ним решай свою судьбу сам. И запомни код для активации антивируса UrFU195rAdi0F4k. Пока, пока...",
            "is_fishing": False}
    ]

    selected_message = None

screen message_list:
    frame:
        xalign 0.5
        yalign 0.35
        vbox:
            for index, msg in enumerate(messages):
                hbox:
                    textbutton "{} {}".format(msg["from"], msg["title"]) action SetVariable("selected_message", index), Hide("message_list"), Show("message_view")
            textbutton "Выйти" action Hide("message_list"), Return("exit_messages")

screen message_view:
    modal True
    frame:
        xalign 0.5
        yalign 0.1
        xsize 600
        vbox:
            if selected_message is not None:
                text "От: [messages[selected_message]['from']]"
                text "[messages[selected_message]['title']]"
                text "[messages[selected_message]['message']]"
                hbox:
                    textbutton "Фишинг" action SetVariable("messages[selected_message]['player_choice']", "phishing"), Hide("message_view"), Return("phishing")
                    textbutton "Нормальное" action SetVariable("messages[selected_message]['player_choice']", "normal"), Hide("message_view"), Return("normal")
            else:
                text "Ошибка"

screen messageview_from_glitch:
    modal True
    frame:
        xalign 0.5
        yalign 0.35
        vbox:
            text "Новое сообщение" yalign 0.1
            text "{glitch=60}Glitch{/glitch}" yalign 0.3
            text "{glitch=40}0ткр0й м0ё с00бщ3ни3{/glitch}" yalign 0.4 xalign 0.1
            hbox:
                xalign 0.5
                yalign 0.8
                textbutton "{glitch=2}Открыть{/glitch}" action Hide("messageview_from_glitch"), Return("opened")
                textbutton "Не открывать" action Hide("messageview_from_glitch"), Return("not_opened")


label minigame_4:
    scene tv
    show screen message_list
    $ result = ui.interact()

    if result == "exit_messages":
        jump after_mini_4
    if result == "phishing":
        "Вы отметили сообщение как фишинговое."
        jump minigame_4
    elif result == "normal":
        "Вы отметили сообщение как нормальное."
        jump minigame_4

label after_mini_4:
    scene room with fade
    show terminal at bounce, center with dissolve:
        yalign 0.0
        zoom 1.0
        linear 0.3 zoom 1.1
    gg "Дааа уж.. Дело набирает большие обороты"
    tr "У вас новое сообщение"
    gg "Опять? Я же только что всё посмотрел"
    scene tv
    show screen messageview_from_glitch
    $ result = ui.interact()

    if result == "opened":
        jump fight_boss
    elif result == "not_opened":
        jump defolt_end

label defolt_end:
    scene black with fade
    gg "К черту это всё. Я уже устал"
    gg "Пора идти"
    scene road-phone with fade
    gg "Ну.. {w=0.5} Всё"
    show 42 at bounce, right with dissolve:
        ypos 1500
        xpos 1500
        zoom 1.2
        linear 0.3 zoom 1.0
    ii "Вот ты уже и закончил свой путь"
    gg "Я уж думал, ты ушёл"
    show 42 at bounce, right with dissolve:
        ypos 1400
        xpos 1500
        linear 0.3 zoom 1.15
    ii "Не мог же я тебя просто так отпустить"
    gg "Даа.. Это было непростое испытание"
    gg "Спасибо, что помогал мне на моем пути"
    if first_choice == "good":
        show 42 at bounce, right:
            ypos 1400
            xpos 1500
        ii "Я верю, что навыки, которые ты здесь получил будут приносить пользу."
        show 42 at bounce, right:
            ypos 1400
            xpos 1500
        ii "Безопасность в вашем цифровом мире очень важна. И есть много мошенников, которые пользуется уязвимостями, чтобы навредить остальным."
        show 42 at bounce, right:
            ypos 1400
            xpos 1500
        ii "Теперь ты сможешь защитить себя и своих близких от такой опасности."
        show 42 at bounce, right:
            ypos 1400
            xpos 1500
        ii "Продолжай и дальше развиваться на своём пути и до встречи"
    elif first_choice == "bad":
        show 42 at bounce, right:
            ypos 1400
            xpos 1500
        ii "Твои навыки взлома, которые ты приобрёл... Это большая сила, в вашем цифровом мире."
        show 42 at bounce, right:
            ypos 1400
            xpos 1500
        ii "Хоть ты и собираешься использовать её для личной выгоды, но помни, что ты не один такой"
        show 42 at bounce, right:
            ypos 1400
            xpos 1500
        ii "Найдутся люди опытнее и сильнее тебя, поэтому не останавливайся на достигнутом"
        show 42 at bounce, right:
            ypos 1400
            xpos 1500
        ii "Может позже ты поймёшь..."
        show 42 at bounce, right:
            ypos 1400
            xpos 1500
        ii "А хотя, это уже твой выбор"
        show 42 at bounce, right:
            ypos 1400
            xpos 1500
        ii "Удачи"
    scene black with fade
    gg "наконец."
    jump the_end

label fight_boss:
    scene black
    gg "Пора избавиться от тебя"
    show glitch with fade
    gl "Как00000йй Н4ивНый Ч3Л0В3333КК 001110 010101 00"

    scene red with fade
    show glitch-front at bounce, center with dissolve:
        yalign 0.0
        zoom 1.0
        linear 0.3 zoom 1.1
    gg "Стой, кажется я знаю, что делать"
    $ ans = renpy.input("{glitch=15}У вас 1 попытка. Введите ключ{/glitch}")
    if ans == "UrFU195rAdi0F4k":
        gl "НЕТ, ЧТО ТЫ СДЕЛАЛ. ОТКУДА ТЫ ЗНАЕШЬ КЛЮЧ"
        gg "Наконец с тобой покончено"
        jump defolt_end
    else:
        gl "Х3Х4хХх444хХ4х4х4х"
        gl "На что ты надеялся, теперь ты станешь частью моей программы"
        gg "ЧЁРТ"
        gg "Теперь я застряну здесь навсегда"
        jump bad_end

label bad_end:
    "Ты почти смог...Попробуй в следующий раз внимательнее читать сообщения от 42"
    jump the_end

label the_end:
    return























screen character_selection():
    tag menu

    frame:
        xalign 0.5
        ypos 25
        text "Выбери своего персонажа"

    hbox:
        xalign 0.5
        yalign 0.5

        imagebutton:
            focus_mask True
            xpos -300
            yalign 0.55
            idle "male_gg_normal.png"
            hover "male_gg_hover.png"
            hovered Play("sound", "audio/sound_hover.mp3")
            action [SetVariable('gg', character_forChoise1), SetVariable('gg_gender', "male"),
                    Play("sound", "audio/sound_selected.mp3"), Jump('start')]

        imagebutton:
            xpos 300
            yalign 0.9
            idle "female_gg_normal.png"
            hover "female_gg_hover.png"
            hovered Play("sound", "audio/sound_hover.mp3")
            action [SetVariable('gg', character_forChoise2), SetVariable('gg_gender', "female"),
                    Play("sound", "audio/sound_selected.mp3"), Jump('start')]
