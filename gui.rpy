################################################################################
## Инициализация
################################################################################

## Установка смещения инициализации заставляет инструкции инициализации в этом файле
## выполняться перед инструкциями инициализации в любом другом файле.
init offset = -2

## Вызов gui.init сбрасывает стили на разумные значения по умолчанию и устанавливает
## ширину и высоту игры.
init python:
    gui.init(1920, 1080)

## Включить проверки на недопустимые или нестабильные свойства в экранах или трансформациях
define config.check_conflicting_properties = True


################################################################################
## Переменные конфигурации GUI
################################################################################


## Цвета ######################################################################
##
## Цвета текста в интерфейсе.

## Акцентный цвет, используемый на протяжении всего интерфейса для обозначения и выделения текста.
define gui.accent_color = '#99ccff'

## Цвет, используемый для текстовой кнопки, когда она не выбрана и не наводится курсор.
define gui.idle_color = '#888888'

## Маленький цвет используется для маленького текста, который нужно сделать ярче/темнее, чтобы
## достичь того же эффекта.
define gui.idle_small_color = '#aaaaaa'

## Цвет, который используется для кнопок и панелей, когда на них наводят курсор.
define gui.hover_color = '#c1e0ff'

## Цвет, который используется для текстовой кнопки, когда она выбрана, но не в фокусе. Кнопка
## считается выбранной, если она является текущим экраном или значением предпочтения.
define gui.selected_color = '#ffffff'

## Цвет, который используется для текстовой кнопки, когда она не может быть выбрана.
define gui.insensitive_color = '#8888887f'

## Цвета, используемые для частей панелей, которые не заполнены. Эти цвета не используются напрямую,
## но применяются при повторной генерации файлов изображений панелей.
define gui.muted_color = '#3d5166'
define gui.hover_muted_color = '#5b7a99'

## Цвета, используемые для текста диалогов и выбора меню.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Шрифт и размеры шрифтов ####################################################

## Шрифт, используемый для текстов в игре.
define gui.text_font = "pixel_font.ttf"

## Шрифт, используемый для имен персонажей.
define gui.name_text_font = "pixel_font.ttf"

## Шрифт, используемый для текстов вне игры.
define gui.interface_text_font = "pixel_font.ttf"

## Размер обычного диалогового текста.
define gui.text_size = 33

## Размер имен персонажей.
define gui.name_text_size = 45

## Размер текста в пользовательском интерфейсе игры.
define gui.interface_text_size = 37

## Размер меток в пользовательском интерфейсе игры.
define gui.label_text_size = 36

## Размер текста на экране уведомлений.
define gui.notify_text_size = 24

## Размер названия игры.
define gui.title_text_size = 75


## Главное и игровое меню #########################################################

## Изображения, используемые для главного и игрового меню.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Диалог ####################################################################
##
## Эти переменные контролируют, как диалог отображается на экране построчно.

## Высота текстового поля, содержащего диалог.
define gui.textbox_height = 278

## Расположение текстового поля по вертикали на экране. 0.0 — верх, 0.5 — центр,
## а 1.0 — низ.
define gui.textbox_yalign = 1.0

## Положение имени говорящего персонажа относительно текстового поля.
## Это может быть целое число пикселей от левого или верхнего края,
## или 0.5 для центрирования.
define gui.name_xpos = 360
define gui.name_ypos = 0

## Горизонтальное выравнивание имени персонажа. Это может быть 0.0 для
## выравнивания по левому краю, 0.5 для центрирования и 1.0 для
## выравнивания по правому краю.
define gui.name_xalign = 0.0

## Ширина, высота и границы бокса, содержащего имя персонажа, или
## None для автоматического определения размеров.
define gui.namebox_width = None
define gui.namebox_height = None

## Границы бокса, содержащего имя персонажа, в порядке:
## левый, верхний, правый, нижний.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Если True, фон бокса с именем будет повторяться; если False, фон
## бокса с именем будет масштабироваться.
define gui.namebox_tile = False



## Размещение диалогов относительно текстового поля. Это может быть целое
## число пикселей относительно левого или верхнего края текстового поля, или 0.5 для центрирования.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Максимальная ширина текста диалога, в пикселях.
define gui.dialogue_width = 1116

## Горизонтальное выравнивание текста диалога. Это может быть 0.0 для выравнивания влево,
## 0.5 для центрирования и 1.0 для выравнивания вправо.
define gui.dialogue_text_xalign = 0.0


## Кнопки #####################################################################
##
## Эти переменные, вместе с файлами изображений в gui/button, контролируют аспекты
## отображения кнопок.

## Ширина и высота кнопки, в пикселях. Если None, Ren'Py вычисляет размер.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(6, 6, 6, 6)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 60

## The vertical position of the skip indicator.
define gui.skip_ypos = 15

## The vertical position of the notify screen.
define gui.notify_ypos = 68

## The spacing between menu choices.
define gui.choice_spacing = 33

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 6

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 15

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 15

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(6, 6, 6, 6)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Vertical borders.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 210

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 173

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 15

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Adjust the location of the textbox.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Change the size and spacing of various things.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
