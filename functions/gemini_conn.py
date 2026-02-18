import asyncio
import google.generativeai as genai
from config.constants import API_KEY, GEMINI_MODEL


genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)
# Словарь для хранения истории: {user_id: [список сообщений]}
user_context = {}

async def ask_gemini(question, user_id):   
    chat_session = user_context[user_id] 
    # Генерация ответа
    response = await asyncio.to_thread(chat_session.send_message, question)
    
    return response.text