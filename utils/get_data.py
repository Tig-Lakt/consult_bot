import os
import sys
import logging
from dotenv import load_dotenv

# Добавляем корневой каталог проекта в PYTHONPATH для удобства импорта
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_PATH)

# Загружаем переменные окружения из файла .env
dotenv_path = os.path.join(PROJECT_PATH, ".env")  # Путь к файлу .env
load_dotenv(dotenv_path, override=True)  # Загружает переменные окружения из .env в os.environ

logging.basicConfig(level=logging.INFO)


def get_bot_token() -> str:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        logging.error("Ошибка: Переменная окружения TELEGRAM_BOT_TOKEN не задана.")
        return None  

    return token


def get_api_key() -> str:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        logging.error("Ошибка: Переменная окружения GEMINI_API_KEY не задана.")
        return None  
    
    return api_key
