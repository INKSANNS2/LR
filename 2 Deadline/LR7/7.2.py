def build_user_profile(user_id: int, **kwargs) -> dict:
    """
    Создает профиль пользователя на основе ID и дополнительной информации.
    Args:
        user_id: Уникальный идентификатор пользователя
        **kwargs: Произвольные именованные аргументы с дополнительной информацией     
    Returns:
        dict: Словарь с профилем пользователя
    """
    profile = {'user_id': user_id}
    for key, value in kwargs.items():
        profile[key] = value
    return profile
profile = build_user_profile(101, name="Анна", status="online", email="anna3453@gmail.com")
print(profile)