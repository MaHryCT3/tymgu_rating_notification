import json
from exceptions import CantGetSettings
from dataclasses import dataclass
from notification import Notification

@dataclass
class Settings:
    repeat_time: int
    UID: str
    page_id: str
    last_position: int
    notifications: list[Notification]

def get_settings(name: str):
    """Получения значения из settings.json"""
    settings = get_settings_dict()
    parametr = settings.get(name, "None")
    if parametr == "None":
        raise CantGetSettings
    return parametr


def get_all_settings() -> Settings:
    settings = get_settings_dict()
    return Settings(**settings)


def get_settings_dict() -> dict:
    """Возвращает веесь словарь со значениями"""
    with open("./settings.json", "r") as settings:
        try:
            return json.load(settings)
        except Exception as e:
            raise CantGetSettings

def set_settings(name, value):
    settings = get_settings_dict()
    if settings.get(name) is None:
        raise ValueError("Указанного параметра не найденно в настройках, добавлять свои нельзя")
    settings[name] = value
    _update_settings_json(settings)


def _update_settings_json(data: dict):
    with open("./settings.json", "w") as settings:
        try:
            json.dump(data, settings, indent=4)        
        except:
            raise # TODO: Добавить какую то ошибку мб, но мне пока лень)
