from utils.get_data import get_bot_token, get_api_key

# Получаем токен бота из переменной окружения(см. utils.py).
TOKEN = get_bot_token()

# Получаем api ключ из переменной окружения(см. utils.py).
API_KEY = get_api_key()

# Константа используемой модели
GEMINI_MODEL = 'gemini-2.5-flash'
