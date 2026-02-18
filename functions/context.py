from functions.gemini_conn import model, user_context




async def get_user_history(user_id):
    if user_id not in user_context:
        user_context[user_id] = []
    return user_context[user_id]


async def reset_user_context(user_id):
    """Сбрасывает историю диалога для пользователя."""
    user_context[user_id] = model.start_chat(history=[])


async def add_to_history(user_id, role, text):
    history = await get_user_history(user_id)
    history.append({
        "role": role,
        "parts": [{"text": text}]
    })
    # Ограничиваем историю (например, последние 10 сообщений)
    if len(history) > 10:
        user_context[user_id] = history[-10:]