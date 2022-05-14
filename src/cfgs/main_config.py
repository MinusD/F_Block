CMD_START = 'начать'
CMD_SCHEDULE = 'бот'

SPLIT_PAIR_SEPARATOR = ' / '
WINDOW_SIGNATURE = '--'
VOID_SIGNATURE = '_'
ONE_PAIR_PATTERN = '{}) {}, {}, {}, {}\n'  # Номер, Предмет, Тип, Преподаватель, Аудитория
ONE_PAIR_SHORT_PATTERN = '{}) {}\n'
ONE_DAY_HEADER_PATTERN = 'Расписание на {}:\n'  #

MONTHS_SLUGS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                'ноября', 'декабря']

ABOUT_TEXT = 'Привет {}!\nЯ бот, который поможет посмотреть расписание, а так же покажет другую ' \
             'полезную информацию\n\n' \
             'Для начала напиши номер своей группы, а я её запомню, что бы больше не приходилось её указывать\n\n'
INVALID_GROUP_TEXT = 'Неверный формат или группы не найдена!\n\nФормат: \'АБВГ-12-34\''
SET_GROUP_TEXT = 'Я запомнил, что ты учишься в группе {}'
CURRENT_GROUP_TEXT = 'Я показываю расписание группы {}'
CURRENT_GROUP_ERROR_TEXT = 'Группа не выбрана, для выбора группы, напишите \n\'{}\' и номер группы'
CURRENT_WEEK_TEXT = 'Идёт {} неделя'
SCHEDULE_SELECT_TEXT = 'Показать расписание ...'

INVALID_COMMAND_TEXT = 'Неизвестная команда\n Что бы получить список команд напиши \'{}\''

BTN_SCHEDULE_TODAY = 'на сегодня'
BTN_SCHEDULE_TOMORROW = 'на завтра'
BTN_SCHEDULE_WEEK = 'на эту неделю'
BTN_SCHEDULE_NEXT_WEEK = 'на следующую неделю'
BTN_WHAT_WEEK = 'неделя?'  # 'Какая неделя?'
BTN_WHAT_GROUP = 'группа?'  # 'Какая группа?'
BTN_SETTINGS = 'настройки'
BTN_HELP = 'помощь'
