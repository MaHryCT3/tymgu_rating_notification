class CantGetRating(Exception):
    """Вызывается когда произошла ошибка при попытке получить позицию в рейтинге"""

class UIDNotFound(Exception):
    """Вызывается, когда по заданному уиду или снилсу не найдено аббитуирентов"""

class CantGetSettings(Exception):
    """Вызывается когда произошла ошибка при попытке получить настройки из файла"""