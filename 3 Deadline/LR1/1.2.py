def make_bold(func):
    """Декоратор, оборачивающий результат в теги <b>"""
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

@make_bold
def get_text():
    return "Hello, World!"
print(get_text()) 