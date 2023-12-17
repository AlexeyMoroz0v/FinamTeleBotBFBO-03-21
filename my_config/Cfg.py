# конфигурационный файл для торговой стратегии


class Config:

    ClientIds = ('599046R8TST',)  # Торговые счета
    AccessToken = 'CAEQ9YxnGhicmlz1kESW9gwB0W5G5bge5FSP2V3zl3k='  # Торговый токен

    Telegram_Token = '6699849772:AAG11R53fQVYghvSVS5JvTBP2OPy6SoxP98'  # токен чат бота от BotFather
    Admin_User_Name = 'Jonn8J'  # управление ботом только от админа username в тг без @
    Chat_Id = '@Jonn8J'  # id кому отправлять сообщения
    user_id = 'Jonn8J'

    FilePath = 'data/'  # путь для сохранения данных
    training_NN = {"SBER", "VTBR"}  # тикеры по которым обучаем нейросеть
    portfolio = ["SBER"]  # тикеры по которым торгуем и скачиваем исторические данные
    security_board = "TQBR"  # класс тикеров

    # доступные M1, M15, H1
    timeframe_0 = "M1"  # таймфрейм для обучения нейросети - вход и на этом же таймфрейме будем торговать
    timeframe_1 = "M15"  # таймфрейм для обучения нейросети - выход
    start = "2021-01-01"  # с какой даты загружаем исторические данные с MOEX

    trading_hours_start = "10:00"  # время работы биржи - начало
    trading_hours_end = "23:50"  # время работы биржи - конец

    # параметры для отрисовки картинок
    period_sma_slow = 64  # период медленной SMA
    period_sma_fast = 16  # период быстрой SMA
    draw_window = 128  # окно данных
    steps_skip = 16  # шаг сдвига окна данных
    draw_size = 128  # размер стороны квадратной картинки
