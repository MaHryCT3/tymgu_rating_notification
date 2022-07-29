import json
from exceptions import CantGetSettings


def get_settings(name: str):
    """Получения значения из settings.json"""
    settings = get_settings_dict()
    parametr = settings.get(name, "None")
    if parametr == "None":
        raise CantGetSettings
    return parametr


def get_settings_dict() -> dict:
    """Возвращает веесь словарь со значениями"""
    with open("./settings.json", "r") as settings:
        try:
            return json.load(settings)
        except Exception as e:
            raise CantGetSettings(e)
        

if __name__ == "__main__":
    print(get_settings("UID"))