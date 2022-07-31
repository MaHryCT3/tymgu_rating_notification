import requests
from typing import Protocol
import os
from exceptions import NoNotificationSettings, AuthorizationError
from dotenv import load_dotenv


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
        self._check_vars()
        self._message = message 
        self._api_link = "https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=Markdownv2".format(
            bot_token=self._token,
            chat_id=self._chat_id,
            message=self._message
        )
    
    def send(self):
        # 401 - ошибка с токеном | 400 - с данными
        response = requests.get(self._api_link)
        status_code = response.status_code
        if status_code == 401:
            raise AuthorizationError
        elif status_code == 400:
            raise ValueError("Скорее всего ошибка с параметрами. Стоит проверить форматер")
        elif status_code != 200:
            raise
                
    
    def _check_vars(self):
        if self._token is None or self._chat_id is None:
            raise NoNotificationSettings


def send_notification(_Notification: Notification) -> None:
    _Notification.send()


if __name__ == "__main__":
    telegram = TelegramNotification("test")
    telegram.send()