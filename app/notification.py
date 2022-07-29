import requests
from typing import Protocol
import os


class Notification(Protocol):
    
    def __init__(self, message: str, *args, **kwargs):
        raise NotImplementedError

    def send(self):
        """Интерфейс для отправки уведомления"""
        raise NotImplementedError
    

class TelegramNotification:
    """Класс для отправки уведомлений в телеграм"""

    def __init__(self, message) -> None:
        self._token = os.getenv("TELEGRAM_TOKEN")
        self._chat_id = os.getenv("TELEGRAM_CHAT_ID")
        #TODO: Добавить вызов ошибки если значения None
        self._message = message 
        self._api_link = "https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=MarkDown".format(
            bot_token=self._token,
            chat_id=self._chat_id,
            message=self._message
        )
    
    def send(self):
        requests.get(self._api_link)  #TODO: Добавить проверку ответа и рейзит если что ошибку


def send_notification(_Notification: Notification) -> None:
    _Notification.send()