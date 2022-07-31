from exceptions import *
from formatter import format_message, MarkDownFormatter
from notification import send_notification, TelegramNotification, Notification
from rating import TymGyRating
from settings import get_settings, set_settings, get_all_settings, Settings
from dotenv import load_dotenv
from repeater import repeater
import logging
import os

load_dotenv(".env")

logger = logging.basicConfig(
    level=os.getenv("LOGER_LEVEL", "INFO"),
    format="%(asctime)s {%(pathname)s}:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S" 
)


Notifications = {
    "Telegram": TelegramNotification
}

Formatters = {
    TelegramNotification: MarkDownFormatter 
}

def get_notifications_list(notifications_settings: list):
    notifications_list = [value for key, value in Notifications.items() if key in notifications_settings]
    if not notifications_list:
        raise NoNotifications
    return notifications_list


def check_changes(rating: TymGyRating, notifications:list [type[Notification]]) -> None:

    new_position = rating.get_rating_position()
    old_position = get_settings("last_position")
    set_settings("last_position", new_position)
    if old_position is None:
        old_position =  new_position
    if new_position != old_position:
        logging.info("Место изменилось с old_position -> new_position")
        run_notification(notifications, new_position, old_position)
    else:
        logging.info("Место в списке не изменилось")
    


def run_notification(notifications: list[type[Notification]], new_position: int, old_position: int):
    for notification in notifications:
        message = format_message(Formatters[notification](
            new_position=new_position, old_position=old_position
        ))
        send_notification(notification(message))
    


def main():
    settings = get_all_settings()
    UID = settings.UID
    page_id = settings.page_id
    rating = TymGyRating(UID=UID, page_id=page_id)
    delay = settings.repeat_time
    notifications_list = get_notifications_list(settings.notifications)
    logging.info(
        f"Уведомления запущены со слующими параметрами - UID:{UID}, page_id:{page_id},"
        f"notifications:{notifications_list}. Проверка будет производиться каждые {delay} секунд.")
    repeater(check_changes, delay, notifications=notifications_list, rating=rating)


if __name__ == "__main__":
    while True:
        try:
            main() #TODO: Добавить обработку всех ошибок, с тектом что нужно возможно нужно сделать для их исправления
        except Exception as e:
            logger.info(e)
