def format_report(report_title: str, *args, **kwargs) -> None:
    """
    Форматирует и выводит отчет с заголовком, данными и свойствами. 
    Args:
        report_title: Название отчета
        *args: Пункты отчета
        **kwargs: Метаданные отчета
    """
    print(f"--- Отчет: {report_title} ---") 
    print("Данные:")
    for item in args:
        print(f" - {item}")  
    print("\nСвойства:")
    for key, value in kwargs.items():
        print(f" - {key}: {value}")  
    print("------------------------------")
format_report(
    "Ежедневный отчет",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    author="Сидоров А.В.",
    date="2025-11-04"
)